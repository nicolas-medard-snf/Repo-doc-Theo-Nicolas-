# Homologous Recombination Deficiency (HRD) Score Predicts Response to Platinum-Containing Neoadjuvant Chemotherapy in Patients with Triple-Negative Breast Cancer

## Metadata

```yaml
---
paper_id: "telli_2016_hrd_score"
title: "Homologous Recombination Deficiency (HRD) Score Predicts Response to Platinum-Containing Neoadjuvant Chemotherapy in Patients with Triple-Negative Breast Cancer"
authors: "Melinda L. Telli, Kirsten M. Timms, Julia Reid, Bryan Hennessy, Gordon B. Mills, Kristin C. Jensen, Zoltan Szallasi, William T. Barry, Eric P. Winer, Nadine M. Tung, Steven J. Isakoff, Paula D. Ryan, April Greene-Colozzi, Alexander Gutin, Zaina Sangale, Diana Iliev, Chris Neff, Victor Abkevich, Joshua T. Jones, Jerry S. Lanchbury, Anne-Renee Hartman, Judy E. Garber, James M. Ford, Daniel P. Silver, Andrea L. Richardson"
year: 2016
venue: "Clinical Cancer Research"
paper_type: "primary_research"
domain: "A_Genomic_Signal"
subdomain: "HRD score (genomic scar: LOH / TAI / LST)"
relevance_score: 5
priority_level: "CRITICAL"
corpus_role: "decision"
temporal_status: "active_candidate"
relevance_tags:
  - "HRD_score"
  - "LOH"
  - "TAI"
  - "LST"
  - "BRCA1"
  - "BRCA2"
  - "TNBC"
  - "platinum"
  - "neoadjuvant"
  - "pCR"
  - "RCB"
  - "genomic_scar"
  - "homologous_recombination_deficiency"
doi: "10.1158/1078-0432.CCR-15-2477"
isbn: ""
url: "http://clincancerres.aacrjournals.org/"
pdf_file: "telli_2016_hrd_score.pdf"
---
```

---

## One-Sentence Summary

In neoadjuvant TNBC trials of platinum-containing therapy, a composite HRD score (LOH + TAI + LST) with predefined threshold ≥42, alone or combined with tumor BRCA1/2 mutation status, predicts pathologic complete response and favorable residual cancer burden — extending platinum sensitivity beyond germline BRCA carriers to sporadic HR-deficient tumors.

---

## Key Contributions

- Validates the **combined HRD score** (unweighted sum of LOH, TAI, and LST) as a pretreatment predictor of neoadjuvant platinum response in TNBC across three independent trial cohorts (PrECOG 0105; pooled cisplatin trials).
- Applies a **predefined HRD threshold of 42** (5th percentile of HRD scores in a BRCA1/2-deficient training set of 497 breast and 561 ovarian tumors) to define HR deficiency jointly with tumor BRCA1/2 mutation.
- Demonstrates that HR deficiency predicts **RCB 0/I and pCR** with large odds ratios in both cohorts, including in **BRCA1/2 wild-type** tumors where high HRD score alone enriches for responders.
- Shows the assay is feasible on **FFPE core biopsies** via an NGS SNP-panel assay (54,091 genome-wide SNPs plus BRCA1/2 coding regions), with HRD scores correlating r = 0.94 between sequencing and MIP SNP arrays.

---

## Core Idea / Mechanism / Argument

### What this paper is (and is not)

This is a **clinical biomarker validation study**, not the original methodological paper defining LOH, TAI, or LST individually. Those genomic-scar metrics were developed in prior work (refs. 17–20: Abkevich et al. 2012 LOH; Birkbak et al. 2012 TAI; Popova et al. 2012 LST; Timms et al. 2014 combined association with BRCA1/2). Telli et al. **operationalize and test** the composite score in TNBC neoadjuvant platinum settings with pCR/RCB endpoints.

### HRD score definition

> HRD score was defined as the unweighted sum of LOH, TAI, and LST scores: HRD = LOH + TAI + LST.

Each component quantifies a distinct pattern of chromosomal-level genomic instability reflecting homologous recombination DNA repair deficiency:

- **LOH**: loss-of-heterozygosity scar (Abkevich et al.)
- **TAI**: telomeric allelic imbalance (Birkbak et al.)
- **LST**: large-scale state transitions (Popova et al.)

### HR deficiency classification

> HR deficiency was defined as high HRD score (above the HRD threshold, ≥ 42) and/or mutated tumor BRCA1/2.

The threshold was **not** tuned on the trial cohorts. It was set on an independent training set (78 breast + 190 ovarian BRCA1/2-deficient tumors among 497 breast and 561 ovarian cases total) to achieve ≥95% sensitivity for detecting BRCA1/2 loss-of-function (mutation with LOH, biallelic mutation, or BRCA1 promoter methylation with LOH):

> To obtain a sensitivity of at least 95%, the threshold was set at the 5th percentile of the HRD scores in this training set of known BRCA1/2-deficient tumors. The 5th percentile of HRD scores was 42 in the combined breast and ovarian training set.

### Argument flow

1. Sporadic TNBC shares DNA-repair defects with BRCA1/2-mutated disease; platinum sensitivity in non-BRCA TNBC motivates a **genomic scar biomarker** beyond mutation testing alone.
2. Individual LOH/TAI/LST metrics associate with BRCA1/2 status, but the **combined HRD score** best distinguishes HR-deficient from intact tumors (prior work cited).
3. HR deficiency (HRD ≥42 or tBRCA1/2 mutation) is tested **prospectively** against centrally assessed RCB 0/I and pCR in platinum neoadjuvant trials.
4. **Claimed**: HR deficiency identifies TNBC — including BRCA1/2 nonmutated tumors — more likely to respond to platinum-containing neoadjuvant therapy.
5. **Demonstrated**: Strong univariate and multivariable associations in two cohorts; improved AUC when HRD is added to stage + tBRCA1/2; assay works on biopsy FFPE.

### Novel vs inherited

| Inherited | Novel in this paper |
|-----------|---------------------|
| LOH, TAI, LST definitions and prior BRCA association (Timms 2014 et al.) | Combined HRD score threshold testing in **independent TNBC neoadjuvant platinum trials** with pCR/RCB endpoints |
| HRD-LOH alone associated with PrECOG 0105 response (prior JCO 2015 abstract/ref 22) | Unified **HR deficiency** predictor (HRD ≥42 OR tBRCA1/2) across PrECOG 0105 + pooled cisplatin trials |
| SNP-based assay platform (Timms 2014) | Multivariable models, BRCA1/2 wild-type subgroup, combined-cohort ROC/AUC analysis |

---

## Methodology / Evidence Base

### Design

- **Type**: Retrospective biomarker analysis embedded in three neoadjuvant **phase II** platinum trials (observational association within trial cohorts).
- **Primary endpoint**: RCB 0/I (yes vs no); **secondary**: pCR (RCB score 0).
- **Predictor**: HR deficiency (HRD ≥42 and/or deleterious/suspected-deleterious tBRCA1/2 mutation).

### Sample / setting

| Cohort | Regimen | Enrolled | Evaluable for HR + response |
|--------|---------|----------|------------------------------|
| PrECOG 0105 | Gemcitabine + carboplatin + iniparib, 4 or 6 cycles | 93 TNBC and/or BRCA1/2 germline-mutation breast cancer | 70 |
| Cisplatin-1 + Cisplatin-2 (pooled) | Cisplatin ± bevacizumab, 4 cycles | 79 stage II–III TNBC | 50 |

PrECOG 0105 is **enriched for BRCA1/2 mutation carriers** (22/68 with passing HRD scores, 32%); cisplatin trials less so (9/47, 19%). All patients had **TNBC** (ER/PR ≤5%, HER2-negative per trial definitions). **HER2+ breast cancer is not studied.**

### Measurements / instruments

- **Pathologic response**: Central RCB index (Symmans et al.); pCR = RCB 0.
- **Molecular assay**: Custom hybridization NGS panel — 54,091 genome-wide SNPs + 685 probes covering BRCA1/2 coding regions (Timms et al. 2014 protocol); allelic imbalance profiles → LOH, TAI, LST → HRD sum.
- **Tissue**: Pretreatment core biopsy FFPE (or frozen); processed at Myriad Genetics under CLIA protocol.
- **BRCA1/2**: Somatic/germline variant and rearrangement detection; only deleterious or suspected-deleterious variants counted.

### Statistical analysis

- Logistic regression for binary RCB 0/I and pCR; OR reported per IQR for continuous HRD or per category.
- Firth's penalized likelihood for pCR models with zero events in HR-nondeficient category (cisplatin cohort).
- Multivariable models adjusted for stage, grade, cycles (PrECOG) or bevacizumab, tumor size, nodal status, age (cisplatin).
- Combined-cohort ROC/AUC for dichotomous HRD; no multiple-testing adjustment (two-sided P at 5%).

### Replication / independence

- Training set for threshold: **fully independent** of all three trial cohorts.
- Cisplatin cohorts: first cohorts where TAI was tested but **not** used in HRD threshold or component development — independent validation of cutoff.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus**: `A_Genomic_Signal` (A1 — HRD / DNA repair genomic scars)
- **Anchor question(s)**: **AQ-1** (genomic features correlated with pCR in neoadjuvant breast cancer); **AQ-3** (high-priority drivers vs background noise — BRCA1/2 and HRD-high define a treatment-relevant feature class beyond single-gene noise)
- **Bridge corpus**: **`E_Study_Type`** — NGS SNP-panel computation of LOH/TAI/LST/HRD from WES/WGS-like SNP profiles; assay inputs and threshold logic. **`B_Therapeutic_Context`** — HRD maps to platinum (and by extension PARP) sensitivity in TNBC neoadjuvant setting.

### How it could be used

- **Directly reusable**: Define HRD score, threshold (≥42), and HR-deficiency call for feature engineering on WES-derived SNP/allelic-imbalance data; use reported ORs and response rates to weight HRD/BRCA1/2 in candidate-gene prioritization for TNBC + platinum neoadjuvant cohorts.
- **Indirectly inspiring**: Pattern of combining three independent genomic-scar metrics into one unweighted sum; bimodal score distribution reducing equivocal mid-range calls.
- **Mainly background / framing**: Rationale linking sporadic TNBC to BRCAness and platinum sensitivity; trial context for carboplatin vs cisplatin regimens.

### Main fit with the project

- One of the strongest **TNBC neoadjuvant pCR** biomarker papers for a **WES-derivable composite signal** (LOH/TAI/LST scars), directly aligned with project endpoint (pCR) and subtype (TNBC).
- Identifies **BRCA1/2** as anchor genes and **HRD-high** as a genome-wide scar capturing HR deficiency in **BRCA1/2 wild-type** responders — critical for AQ-3 noise filtering.

### Main mismatch or risk

- **Subtype**: TNBC only; no HER2+ cohort — cannot generalize HRD→pCR claims to HER2+ without separate evidence.
- **Regimen specificity**: All arms include **platinum**; HRD predicts platinum response, not generic neoadjuvant chemo — misapplying to anthracycline/taxane-only regimens is a failure mode (authors note possible broader DNA-damage agent association but do not demonstrate it here).
- **No control arm** without platinum; predictive value for *adding* platinum vs standard SOC is not established in these trials.
- **Industry assay**: Myriad Genetics co-authors and IP; threshold and panel design tied to commercial test — WES-only pipelines may need harmonization (see `E_Study_Type`).
- PrECOG 0105 includes **iniparib** (later failed PARP-like agent); cisplatin cohort is small (N=50 evaluable) with wide CIs for pCR.

### Concrete follow-up

- Ingest **Timms et al. 2014** (`timms_2014_brca_hrd_scores`) for methodological foundation of LOH/TAI/LST computation and training-set derivation.
- Cross-link **`B_Therapeutic_Context`**: platinum neoadjuvant TNBC; PARP inhibitor sensitivity literature for HRD-high sporadic disease.
- Cross-link **`C_Cancer_Subtype`**: gate all HRD claims to TNBC (and BRCA1/2-associated breast cancer in PrECOG subset).
- Cross-link **`D_Clinical_Endpoint`**: pCR and RCB 0/I definitions; compare effect sizes with other TNBC pCR predictors.
- For WES feature extraction: map project pipeline outputs to LOH/TAI/LST components or validated HRD proxy; verify threshold transferability on non-Myriad data.

---

## Assumptions

- Loss of BRCA1/2 function (mutation or BRCA1 methylation with LOH) is a valid gold standard for HR deficiency in the training set; the 5th-percentile HRD score in that set approximates HR deficiency from any cause.
- Unweighted sum of LOH + TAI + LST is sufficient; no weighting by component improves prediction (inherited from prior work, not re-optimized here).
- HRD threshold ≥42 generalizes from mixed breast/ovarian training data to TNBC platinum trials despite different tumor types in threshold derivation.
- tBRCA1/2 mutation on the SNP panel captures clinically relevant HR deficiency alongside HRD score; variants of uncertain significance are treated as non-mutated.
- RCB 0/I and pCR are adequate surrogates for clinical benefit in neoadjuvant TNBC (RCB validated prognostically elsewhere).
- Pretreatment core biopsy adequately represents tumor HRD status (no spatial heterogeneity analysis).

---

## Limitations / Failure Modes

- **No non-platinum comparator arm** — cannot prove HRD selects patients who benefit specifically from platinum addition vs standard therapy.
- **Small evaluable samples** (N=70 and N=50) and **zero pCR events** in HR-nondeficient cisplatin arm — unstable pCR OR estimates (Firth correction used).
- **Assay failure rate**: HRD score failed in 21% (PrECOG) and 18% (cisplatin) of submitted samples — clinical deployment would leave substantial "undetermined" cases.
- **PrECOG 0105 confounding**: Enrichment for BRCA1/2 carriers and multi-agent regimen (gemcitabine + carboplatin + iniparib) differs from cisplatin monotherapy cohorts; combined analyses require cohort adjustment.
- **BRCA1/2 wild-type subgroup in PrECOG**: High HRD vs low HRD trends for RCB 0/I (P=0.062) and pCR (P=0.063) were **not statistically significant** at α=0.05 — sporadic HRD claim rests more heavily on cisplatin pooled data (P=0.0039 / 0.018).
- **Multiple testing**: No adjustment across endpoints and subgroups — some associations may be inflated.
- **Commercial conflict**: Multiple authors affiliated with or funded by Myriad Genetics; TAI patent licensed to Myriad — independent replication on academic WES pipelines recommended.

---

## Key Quantitative or Qualitative Results

### HR deficiency vs response (Table 1)

**PrECOG 0105 (N=70)**

| Outcome | HR-deficient | HR-nondeficient | OR (95% CI) | P |
|---------|--------------|-----------------|-------------|---|
| RCB 0/I | 34/50 (68%) | 6/20 (30%) | 4.96 (1.61–15.3) | 0.0036 |
| pCR | 21/50 (42%) | 2/20 (10%) | 6.52 (1.36–31.2) | 0.0058 |

**Pooled cisplatin trials (N=50)**

| Outcome | HR-deficient | HR-nondeficient | OR (95% CI) | P |
|---------|--------------|-----------------|-------------|---|
| RCB 0/I | 15/29 (51.7%) | 2/21 (9.5%) | 10.18 (2.00–51.89) | 0.0011 |
| pCR | 8/29 (27.5%) | 0/21 (0%) | 17.00 (1.91–2249) | 0.0066 |

### Multivariable models (Table 3)

- PrECOG RCB 0/I: HR deficiency OR **5.86** (1.33–25.7), P=**0.012** after stage, grade, cycles, age.
- Cisplatin RCB 0/I: HR deficiency OR **12.1** (1.97–74.0), P=**0.0017** after bevacizumab, size, nodal status, age.
- Cisplatin pCR: HR deficiency P=**0.0063**; age at diagnosis P=**0.026**.

### BRCA1/2 wild-type, high HRD (≥42) vs low (Table 2B)

- Cisplatin: RCB 0/I 52.6% vs 10.5%, OR 9.44, P=**0.0039**; pCR 26.3% vs 0%, OR 14.79, P=**0.018** (N=38).
- PrECOG: RCB 0/I 59% vs 32%, P=0.062; pCR 33% vs 11%, P=0.063 (N=46) — borderline.

### ROC / threshold performance

- Combined cohorts: AUC **0.761** (RCB 0/I), **0.747** (pCR) for HRD score.
- Sensitivity at threshold 42: **85%** (RCB 0/I), **93%** (pCR).
- BRCA1/2-mutated sample detection at ≥42: **26/27 (96.3%)** vs 95% training target.

### Training set HRD distribution (Figure 1)

- BRCA-intact (n=790): median HRD **22**, 5th percentile **2**.
- BRCA-deficient (n=268): median HRD **64**, 5th percentile **42** (threshold).

---

## Key Quotes

> "Recently, three independent DNA-based measures of genomic instability were developed on the basis of loss of heterozygosity (LOH), telomeric allelic imbalance (TAI), and large-scale state transitions (LST)."

> "We assessed a combined homologous recombination deficiency (HRD) score, an unweighted sum of LOH, TAI, and LST scores, in three neoadjuvant TNBC trials of platinum-containing therapy."

> "HR deficiency, defined as HRD score ≥42 or BRCA1/2 mutation, with response to platinum-based therapy."

> "HRD score was defined as the unweighted sum of LOH, TAI, and LST scores: HRD = LOH + TAI + LST."

> "To obtain a sensitivity of at least 95%, the threshold was set at the 5th percentile of the HRD scores in this training set of known BRCA1/2-deficient tumors. The 5th percentile of HRD scores was 42 in the combined breast and ovarian training set."

> "HR deficiency was significantly associated with both RCB 0/I and pCR in both the PrECOG 0105 and cisplatin trials cohorts."

> "When restricted to BRCA1/2 nonmutated tumors, response was higher in patients with high HRD scores."

> "The distribution of HRD scores in the training set used to establish the HRD score cutoff and in the two neoadjuvant cohorts analyzed here is bimodal, with fewer tumors with scores around the cut-off point."

> "In this analysis, HRD status provides significant improvement over clinical variables or BRCA1/2 mutation status in identifying tumors with an increased likelihood of response to platinum-based neoadjuvant therapy among patients with TNBC."

> "The clinical trials described here do not include a nonplatinum comparator arm."

---

## Cross-References

### Complements entries in corpus

- **`timms_2014_brca_hrd_scores`** (to ingest, ref. 20): Defines SNP-panel assay, LOH/TAI/LST components, and BRCA1/2 association in training cohorts — upstream methodology for this validation paper.
- **`abkevich_2012_loh`**, **`birkbak_2012_tai`**, **`popova_2012_lst`** (to ingest): Individual genomic-scar metrics that compose HRD.

### Contradicts / Tensions

- None within corpus yet. **Tension to monitor**: HRD may predict response to non-platinum DNA-damaging agents (anthracyclines/alkylators per GeparSixto cited in Discussion) — would blur **`B_Therapeutic_Context`** platinum specificity if confirmed.

### Cross-corpus connections

- **`E_Study_Type`**: NGS SNP enrichment panel (54,091 SNPs), allelic imbalance profiling, HRD computation pipeline — method prerequisite for extracting HRD from sequence data.
- **`B_Therapeutic_Context`**: Platinum (carboplatin, cisplatin) neoadjuvant TNBC; implicit PARP-inhibitor relevance via HR deficiency biology.
- **`C_Cancer_Subtype`**: TNBC-only evidence; PrECOG also enrolled BRCA1/2 germline-mutation breast cancer with TNBC-like treatment.
- **`D_Clinical_Endpoint`**: pCR (RCB 0) and RCB 0/I as primary/secondary endpoints with centrally reviewed pathology.

### Related entries to add

- **HIGH**: Timms et al. 2014 — HRD score methodology and training-set derivation.
- **HIGH**: Telli et al. 2015 J Clin Oncol (PrECOG 0105 primary trial) — clinical context for biomarker substudy.
- **HIGH**: GeparSixto / von Minckwitz HRD substudies — platinum in TNBC randomized context.
- **MEDIUM**: Silver et al. 2010, Ryan et al. 2009 — cisplatin neoadjuvant TNBC parent trials.
- **MEDIUM**: Marquard et al. 2015 pan-cancer HRD scar analysis.

---

## Author Notes

### Priority justification

**CRITICAL** — First full peer-reviewed validation linking the **combined HRD score (LOH+TAI+LST)** with **pCR and RCB** in **neoadjuvant platinum-treated TNBC**, with explicit threshold, multivariable models, and BRCA1/2 wild-type subgroup. Directly anchors A1 HRD feature class for the project's TNBC pCR prediction goal.

### Use this source for

- Defining HRD score, components (LOH, TAI, LST), and ≥42 threshold in project documentation.
- Evidence that HR deficiency (HRD-high or tBRCA1/2) enriches for **pCR** under platinum neoadjuvant therapy in TNBC.
- Prioritizing **BRCA1**, **BRCA2**, and **HRD-high scar status** as high-value features (AQ-3).
- Assay feasibility on **pretreatment biopsy FFPE** for neoadjuvant setting.
- Effect-size benchmarks (OR ~5–17 for HR deficiency vs response).

### Do NOT use this source for

- HER2+ breast cancer HRD→pCR claims → no data in this paper.
- Non-platinum neoadjuvant regimens as primary evidence → platinum-specific; broader chemo associations are hypothesized only.
- Step-by-step LOH/TAI/LST algorithm implementation → use Timms 2014 and component papers (`E_Study_Type`).
- PARP inhibitor neoadjuvant pCR → platinum trials only; PARP link is biological inference.
- Proving platinum should be added to SOC → no randomized non-platinum control.

### Curation notes

- Document identity confirmed: **Telli et al. 2016, Clin Cancer Res** — clinical validation of combined HRD score, not the original LOH/TAI/LST methods paper.
- Harmonize **HRD ≥42** vs **HRD ≥ 42** notation; **HR deficiency** = HRD-high OR tBRCA1/2 mutant.
- Index under: HRD score, LOH, TAI, LST, BRCA1/2, TNBC, platinum, pCR, neoadjuvant.
- Multiple Myriad Genetics co-authors; flag for independent academic replication when applying to in-house WES.
- PrECOG 0105 includes iniparib — note regimen heterogeneity when pooling with cisplatin trials.

---

## Related Concepts

homologous recombination deficiency, HRD score, HRD-LOH, loss of heterozygosity, LOH, telomeric allelic imbalance, TAI, large-scale state transitions, LST, genomic scar, BRCA1, BRCA2, BRCAness, triple-negative breast cancer, TNBC, platinum chemotherapy, carboplatin, cisplatin, neoadjuvant therapy, pathologic complete response, pCR, residual cancer burden, RCB, allelic imbalance, SNP panel, FFPE biopsy, DNA repair deficiency, sporadic HR deficiency

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
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated *(deferred per ingestion task — see suggested additions)*
- [ ] the corpus `README.md` registry and counts have been updated *(deferred per ingestion task — see suggested additions)*
