# HRDetect is a predictor of BRCA1 and BRCA2 deficiency based on mutational-signatures

## Metadata

```yaml
---
paper_id: "davies_2017_hrdetect"
title: "HRDetect is a predictor of BRCA1 and BRCA2 deficiency based on mutational-signatures"
authors: "Helen Davies, Dominik Glodzik, Sandro Morganella, Lucy R. Yates, Johan Staaf, Xueqing Zou, Manasa Ramakrishna, Sancha Martin, Sandrine Boyault, Anieta M. Sieuwerts, Peter T. Simpson, Tari A. King, Keiran Raine, Jorunn E. Eyfjord, Gu Kong, Åke Borg, Ewan Birney, Hendrik G. Stunnenberg, Marc J. van de Vijver, Anne-Lise Børresen-Dale, John W.M. Martens, Paul N. Span, Sunil R Lakhani, Anne Vincent-Salomon, Christos Sotiriou, Andrew Tutt, Alastair M. Thompson, Steven Van Laere, Andrea L. Richardson, Alain Viari, Peter J Campbell, Michael R. Stratton, Serena Nik-Zainal"
year: 2017
venue: "Nature Medicine"
paper_type: "methodological"
domain: "A_Genomic_Signal"
subdomain: "HRD / mutational signatures"
relevance_score: 5
priority_level: "CRITICAL"
corpus_role: "decision"
temporal_status: "active_candidate"
relevance_tags:
  - "HRDetect"
  - "BRCA1"
  - "BRCA2"
  - "HRD"
  - "mutational_signatures"
  - "SBS3"
  - "SBS8"
  - "rearrangement_signatures"
  - "lasso_logistic_regression"
  - "WGS"
  - "WES_limitations"
  - "BRCAness"
  - "PARP_inhibitor_stratification"
doi: "10.1038/nm.4292"
isbn: ""
url: "https://doi.org/10.1038/nm.4292"
pdf_file: "davies_2017_hrdetect.pdf"
---
```

---

## One-Sentence Summary

Davies et al. (2017) define **HRDetect**, a lasso logistic-regression classifier integrating six WGS-derived mutational-signature and HRD-scar features that detects biallelic BRCA1/BRCA2 deficiency with AUC 0.98 and 98.7% sensitivity, revealing up to ~22% of breast cancers as HR-deficient beyond the ~1–5% with known germline mutations — directly relevant to extracting an HRD genomic signal from sequencing for neoadjuvant stratification, with critical caveats for WES-only pipelines.

---

## Key Contributions

- Demonstrates that **BRCA1/BRCA2 deficiency produces a composite genomic phenotype** spanning base-substitution signatures (SBS3, SBS8), indels with microhomology, rearrangement signatures (RS3, RS5), and HRD copy-number scars — not a single signature.
- Builds **HRDetect**, a supervised lasso logistic regression model with non-negative coefficients that outputs a probabilistic BRCA1/BRCA2-deficiency score from log-transformed, z-scored signature exposures.
- Applies HRDetect to **560 WGS breast cancers**, identifying 124 samples (22%) above the 70% probability cutoff, including 47 without detectable biallelic BRCA1/BRCA2 mutation or promoter methylation.
- Validates generalizability across **80 independent WGS breast cancers**, **73 ovarian**, and **96 pancreatic** cancers; tests **low-coverage WGS (10×)**, **WES**, **FFPE**, and a small **neoadjuvant TNBC biopsy** cohort.
- Shows HRDetect **outperforms HRD score alone** (60% sensitivity) and any individual signature, establishing multi-signature integration as the operative mechanism.

---

## Core Idea / Mechanism / Argument

### Claimed vs demonstrated

**Claimed:** Mutational signatures are a direct physiological readout of HR pathway abrogation; integrating all signature classes yields a classifier whose performance "is unlikely to be bettered" for detecting BRCA1/BRCA2 deficiency and broader "BRCAness," with implications for PARP-inhibitor and platinum stratification beyond germline mutation carriers.

**Demonstrated:** On WGS data with matched normal, biallelic BRCA1/BRCA2 inactivation (germline, somatic, or BRCA1 promoter hypermethylation with LOH) produces a reproducible multi-class mutational footprint. A sparse lasso logistic model trained on 77 positive vs 234 quiescent sporadic controls selects six independent positive-weight features. Applied at a 0.7 probability threshold, the final HRDetect model achieves AUC 0.98 and 98.7% sensitivity against verified biallelic status in the 560-cohort ROC analysis (371 samples with complete methylation/HRD annotation). Cross-cohort and down-sampling experiments support robustness; WES-only application materially degrades sensitivity unless retrained.

### Information flow

1. **WGS + matched normal** → somatic variant calling (CaVEMan substitutions, Pindel indels, BRASS rearrangements) + SNP6/ASCAT copy number.
2. **Signature decomposition** — 12 SBS, 2 indel, 6 rearrangement signatures via NMF/COSMIC exposure assignment; HRD index from allele-specific copy number.
3. **Feature engineering** — log-transform counts (`log(x+1)`), z-normalize per feature across training set.
4. **Supervised learning** — lasso logistic regression (`glmnet`, non-negative β) with nested 10-fold cross-validation; iterative retraining as hidden biallelic cases are discovered (22 → 77 positives).
5. **Scoring** — logistic function on normalized exposures with learned intercept β₀ = −3.364; probability ≥ 0.7 = HR-deficient call.
6. **Biological interpretation** — high-score, mutation-negative tumours interpreted as functional HR deficiency ("BRCAness") potentially PARP/platinum-sensitive.

### Novel vs inherited

- **Inherited:** Prior work linked SBS3 to BRCA1/BRCA2 null tumours (Nik-Zainal et al.; Alexandrov COSMIC signatures); HRD genomic scar indices (Abkevich, Natrajan); 560-breast WGS landscape (Nik-Zainal et al. 2016 Nature).
- **Novel:** Quantitative multi-signature integration via constrained lasso; formal HRDetect algorithm with published coefficients; systematic enumeration of hidden biallelic carriers; explicit WGS vs WES vs low-coverage performance comparison; neoadjuvant biopsy pilot linking HRDetect to treatment response.

### Final HRDetect feature weights (77-sample training)

| Feature | Coefficient (β) |
|---------|-----------------|
| Microhomology-mediated indels (>3 bp) | 2.398 |
| Base substitution Signature 3 | 1.611 |
| Rearrangement Signature 3 (short tandem duplications <10 kb) | 1.153 |
| Rearrangement Signature 5 (non-clustered deletions <100 kb) | 0.847 |
| HRD index | 0.667 |
| Base substitution Signature 8 | 0.091 |

---

## Methodology / Evidence Base

### Design
Methodological primary research built on observational WGS cohorts; supervised machine-learning classifier development with nested cross-validation and independent validation cohorts.

### Sample / setting

| Cohort | N | Context |
|--------|---|---------|
| Primary training/discovery | 560 | WGS breast cancers (ICGC/BASIS consortium); 22 initial germline BRCA1/BRCA2 with LOH |
| Expanded training positives | 77 | Biallelic BRCA1/BRCA2 inactivation (germline, somatic, BRCA1 methylation) |
| Sporadic controls | 234–235 | Manually curated "quiescent" sporadic genomes without BRCA signatures |
| ROC evaluation subset | 371 | Samples with methylation + HRD data for verified BRCA status |
| Validation breast | 80 | Independent WGS, mainly ER+, HER2− |
| Ovarian | 73 | WGS chemoresistant ovarian |
| Pancreatic | 96 | WGS pancreatic |
| Neoadjuvant pilot | 9 TNBC | Anthracycline ± taxane neoadjuvant; 18 DNA samples (biopsies + resections) |
| Down-sampled WGS | 560 | In silico 10× coverage (9.9–10.5×) |

Sequencing: 30–40× WGS on tumour + normal; GRCh37; BWA alignment.

### Measurements / instruments

- **Mutations:** CaVEMan (SNV), Pindel (indels), BRASS (SVs) — 3,479,652 substitutions, 371,993 indels, 77,695 rearrangements across 560 samples.
- **Signatures:** 96-channel SBS exposure via iterative COSMIC signature assignment; RS1–RS6 rearrangement classes; 2 indel signature classes.
- **Copy number / HRD:** Affymetrix SNP6 + ASCAT allele-specific profiles → HRD index (R implementation per Abkevich/Natrajan).
- **BRCA status ground truth:** Germline/somatic variant calling, MLPA, promoter methylation arrays; biallelic inactivation required for positive labels.

### Statistical analysis approach

- Lasso logistic regression with L1 penalty λ selected by nested CV (`glmnet`).
- Non-negativity constraint on all β weights (biological: signatures mark presence of HR-deficiency processes).
- 10-fold nested CV for robustness; 100× subsampling stability checks.
- Interaction terms tested — no improvement over additive model.
- ROC/AUC, sensitivity at 0.7 cutoff; Pearson correlation for coverage concordance.

### Replication or pre-registration status

No pre-registration. Independent 80-sample breast validation cohort; cross-tissue validation (ovarian, pancreatic). Algorithm coefficients in Supplementary Tables 13–14.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus:** `A_Genomic_Signal` (A1 — HRD / mutational signatures / DNA repair)
- **Anchor question(s):** Primarily **AQ-1** (WES-derivable mutational drivers/signals correlated with treatment response) and **AQ-3** (prioritizing high-priority HR-pathway signal vs genomic noise)
- **Bridge corpus:** `B_Therapeutic_Context` (HRDetect stratifies PARP-inhibitor/platinum/anthracycline-sensitive BRCAness); `E_Study_Type` (HRDetect as a computational WGS/WES predictor requiring specific calling and signature pipelines)

### How it could be used

- **Directly reusable:** HRDetect probability score and its six constituent features define the **HRD composite genomic signal** extractable from sequencing — the project's primary A1 feature class for DNA-repair deficiency. Coefficients, normalization equations, and 0.7 cutoff are implementable given WGS-level inputs.
- **Indirectly inspiring:** The neoadjuvant TNBC biopsy pilot (4/4 complete responders with high HRDetect vs 5/5 residual disease with low scores) motivates testing HRDetect against **pCR** even though this paper's primary endpoint is BRCA status, not pCR.
- **Mainly background / framing:** Population prevalence arguments (~22% HR-deficient breast cancers) and PARP-inhibitor trial stratification rhetoric — useful context but not pCR-validated.

### Main fit with the project

HRDetect operationalizes **what "HRD" means at the feature level** for WES/WGS pipelines: not a single gene but a weighted combination of SBS3, SBS8, RS3, RS5, microhomology indels, and HRD index. For TNBC neoadjuvant response prediction, the paper explicitly analyzes pretreatment needle biopsies from anthracycline-treated TNBC patients and links high HRDetect to complete pathological response — the closest available bridge to the project's pCR endpoint within this source. The demonstration that monoallelic BRCA1/BRCA2, PALB2, ATM, ATR mutations **do not** reliably produce high HRDetect scores supports **AQ-3 deprioritization** of single-allele HR-gene hits as noise unless biallelic.

### Main mismatch or risk

- **WES vs WES project assumption:** The project's working modality is WES, but HRDetect was designed and optimized on **WGS**. Native WES application drops sensitivity to **46.8%**; WES-retrained model reaches **73%** at the cost of 12 false positives — rearrangement signatures RS3/RS5 are unavailable on exome-only data.
- **Endpoint mismatch:** Primary validation is **BRCA1/BRCA2 biallelic status**, not neoadjuvant pCR. The neoadjuvant analysis is n=9 (4 responders) — underpowered for the project's core endpoint.
- **Subtype mix:** The 560-cohort spans all breast subtypes; neoadjuvant pilot is TNBC-only with anthracyclines, not PARP inhibitors or HER2-targeted regimens central to the project.
- **Resistance caveat:** Authors note resistant tumours retaining historic HR-deficiency scars may score high despite acquired resistance alleles.

### Concrete follow-up

1. When building WES feature extraction, implement the **WES-retrained HRDetect variant** (Supplementary Table 7) or explicitly document missing RS3/RS5 as a known sensitivity loss.
2. Cross-reference with `B_Therapeutic_Context` entries on PARP/platinum sensitivity and `D_Clinical_Endpoint` for any pCR-validated HRD studies in TNBC/HER2+.
3. Flag **BRCA1, BRCA2** and pathway genes (PALB2, BRIP1) as conditional high-priority only with **biallelic inactivation** evidence, per HRDetect ground-truth logic.
4. Seek dedicated TNBC/HER2+ neoadjuvant pCR studies using HRDetect or constituent signatures for direct AQ-1 validation.

---

## Assumptions

- Biallelic BRCA1/BRCA2 inactivation (or BRCA1 promoter methylation with LOH) is the appropriate **ground truth** for HR deficiency; tumours scoring high without canonical mutations are assumed functionally HR-deficient ("BRCAness").
- Sporadic breast cancers with "quiescent" genome plots represent true HR-proficient negatives — manual curation introduces selector bias.
- Mutational signatures are **stable scars** reporting cumulative HR deficiency rather than transient repair competence.
- Non-negative lasso coefficients are biologically valid: HR-deficiency signatures never invert to negative predictors.
- Matched normal DNA is available for somatic calling; FFPE and low-cellularity (≥15%) samples remain scorable.
- The 0.7 probability threshold is fixed across tissues; authors acknowledge tissue-specific retuning may be needed.
- PARP/platinum/anthracycline sensitivity is inferred from HRDetect–BRCA concordance, not directly proven at scale in this paper.

---

## Limitations / Failure Modes

- **WES incompatibility:** Rearrangement signatures RS3 and RS5 — among the highest-weight features — cannot be measured on exome data; WES sensitivity 46.8% with WGS-trained weights.
- **Hidden positives among high-score negatives:** ~47/124 high-score samples lack verified biallelic BRCA1/BRCA2 or methylation; ~30% of high-score calls are genetically unauthenticated — functional HR deficiency is inferred, not proven.
- **BRCA1 underrepresentation in training:** Only 5/22 initial BRCA1 tumours caused 6 BRCA1-null samples to score 0.006–0.64; RS3 (BRCA1-enriched) is less stable across CV folds.
- **Monoallelic HR-gene mutations:** Germline/somatic monoallelic BRCA1/BRCA2, PALB2, ATM, ATR, CHEK2, RAD51C, etc. generally yield **low** HRDetect scores despite moderate-penetrance risk — single-allele calls are poor HRD proxies.
- **Resistance / historic scars:** Acquired reversion mutations may not lower HRDetect if mutational scars persist.
- **Small neoadjuvant n:** Treatment-response association (n=9) is hypothesis-generating only.
- **Commercial/IP:** Authors are patent applicants on HRDetect; algorithm access may require licensing.

---

## Key Quantitative or Qualitative Results

| Metric | Value | Notes |
|--------|-------|-------|
| AUC (560 breast, ROC on 371 verified) | **0.98** | vs HRD score alone ~0.85 effective (60% sensitivity) |
| Sensitivity at 0.7 cutoff (560 cohort) | **98.7%** | Abstract and main text |
| High-score prevalence (560 breast) | **124/560 (22%)** | vs ~1–5% known germline carriers |
| Hidden biallelic discoveries | +33 germline, +22 somatic/methylated | Beyond 22 recruited carriers |
| Mutation-negative high scores | **47** | No biallelic BRCA1/BRCA2 or methylation |
| Validation breast (80 WGS) | **86% sensitivity** | 6/7 biallelic detected; 1 BRCA1 splice missed |
| Low-coverage WGS (10×) | **86% sensitivity**; r=0.96 vs high-coverage | HRD score concordance r=0.63 |
| WES (WGS weights) | **46.8% sensitivity** | Missing rearrangement features |
| WES (retrained) | **73% sensitivity (56/77)** | +12 false positives |
| Ovarian (73) | **~100% sensitivity**; 63% prevalence at 0.7 | 16 additional HR-deficient beyond known |
| Pancreatic (96) | **~100% sensitivity** on confirmed biallelic | 5 additional potential HR-deficient |
| Neoadjuvant TNBC | **4/4 CR high HRDetect; 5/5 residual low** | Anthracycline ± taxane; n=9 |
| FFPE germline BRCA1 | Score **0.94** | Despite absent SBS3 from FFPE artifact |
| Cross-validation AUC (77 vs 234 training) | **1.0** | Nested CV on training subset |

---

## Key Quotes

> "A supervised lasso logistic regression model to identify six critically distinguishing mutational signatures predictive of BRCA1/BRCA2 deficiency."

> "A defect in a single gene such as BRCA1/BRCA2 does not result in a single signature – it gives rise to at least five mutational signatures of all classes, including base substitutions, indels and rearrangements."

> "Unlike most biomarkers, these multiple mutational signatures are the direct consequence of abrogation of DSB repair pathways."

> "HRDetect identifies BRCA1/BRCA2 deficient samples with 98.7% sensitivity (AUC 0.98)."

> "In particular, it is superior to current methods of assessing BRCA1/BRCA2 deficiency, specifically, the genomic 'scar' based index like the HRD score (sensitivity of HRD score = 60%)."

> "When HRDetect is used to assess BRCA1/BRCA2 deficiency on data that are representative of only coding sequences (whole exome sequencing, WES), the sensitivity of detection is affected considerably falling to 46.8%. This is because essential predictor components such as rearrangement signatures 3 and 5 are not available by WES."

> "Nearly a third of tumours with high scores for BRCA1/BRCA2 deficiency scores cannot be authenticated as BRCA1/BRCA2 null through genetic/epigenetic means. Yet, given the striking resemblance to BRCA1/BRCA2 null tumours, it is intriguing to consider that these cancers are therefore biologically comparable and likely to respond similarly to BRCA1/BRCA2 null cancers, in particular to PARP-inhibition."

> "Interestingly, four patients demonstrated complete responses to treatment and all had high HRDetect scores – two were confirmed to be germline BRCA1 mutation carriers and two were sporadic tumours. By contrast, five patients that exhibited residual disease had low HRDetect probability scores."

> "We constrained all β weights to be positive because they reflect the biological presence of mutational processes that are due to (in this case) BRCA1/BRCA2 deficiency."

> "Our analyses also emphasise that a WGS approach (even if at low-coverage (10 fold)) is far more effective than a WES approach at detecting BRCA1/BRCA2 deficiency."

---

## Cross-References

### Complements entries in corpus
- _(pending)_ `nik_zainal_2016_560_breast_wgs`: upstream WGS landscape and signature catalog HRDetect is built upon.
- _(pending)_ `alexandrov_2013_cosmic_signatures`: COSMIC mutational signature framework used for SBS exposure assignment.

### Contradicts / Tensions
- **Single-signature SBS3 approaches:** Paper explicitly states SBS3 alone lacks a straightforward discriminatory cutoff; multi-signature integration required.
- **HRD score / scar-only methods:** HRDetect sensitivity 98.7% vs HRD score 60% on same cohort — tension for projects using HRD index alone on WES SNP arrays.
- **Monoallelic HR-gene testing:** Clinical panels reporting PALB2/ATM/CHEK2 variants without LOH evidence may over-call HRD that HRDetect would score as proficient.

### Cross-corpus connections
- **`B_Therapeutic_Context`:** HRDetect-positive tumours linked to PARP-inhibitor, platinum, anthracycline, and mitomycin C sensitivity — maps HRD signal to neoadjuvant drug classes.
- **`E_Study_Type`:** HRDetect defines required bioinformatics pipeline (CaVEMan/Pindel/BRASS, signature exposure, ASCAT/HRD index, glmnet scoring) — method dependency for any A1 feature extraction.
- **`D_Clinical_Endpoint`:** Neoadjuvant TNBC biopsy pilot links HRDetect to **complete pathological response** (not formal pCR terminology but equivalent) — bridge for endpoint validation.
- **`C_Cancer_Subtype`:** High-score enrichment in ER− (42/143) vs ER+ (5/340); neoadjuvant data TNBC-specific.

### Related entries to add
- **HIGH:** Nik-Zainal et al. 2016 Nature (560 breast WGS landscape) — upstream data resource.
- **HIGH:** Watkins/Tutt HRD scar review (Breast Cancer Res 2014) — comparator method cited.
- **HIGH:** Graeser et al. 2010 (RAD51 foci → pCR) — functional HR assay linked to neoadjuvant response.
- **MEDIUM:** Lord & Ashworth 2016 "BRCAness revisited" — conceptual framing cited.
- **MEDIUM:** Yates et al. 2015 multiregion sequencing — biopsy/resection concordance context.

---

## Author Notes

### Priority justification
**CRITICAL** because HRDetect is the project's named HRD extraction method (per `project_overview.md` §6) and defines the operative multi-signature feature vector for A1. It specifies which genomic measurements matter, their weights, WES limitations, and the only in-paper neoadjuvant response association available for TNBC.

### Use this source for
- Defining the **HRD composite signal** and its six weighted components for WGS/WES pipelines
- Setting **BRCA1/BRCA2 biallelic inactivation** as the canonical positive label for HRD feature validation
- Understanding **WES sensitivity trade-offs** when planning exome-based feature extraction
- Interpreting **high HRDetect / low mutation** tumours as functional BRCAness candidates
- Neoadjuvant **biopsy-level** HRDetect feasibility and concordance across specimens
- Deprioritizing **monoallelic HR-gene variants** as standalone HRD markers

### Do NOT use this source for
- **Definitive pCR prediction in HER2+ or large TNBC cohorts** → seek dedicated neoadjuvant pCR studies; n=9 anthracycline pilot only
- **WES-optimal HRD calling without retraining** → WES sensitivity 46.8% with WGS weights; use Supplementary WES model or accept performance loss
- **PARP-inhibitor response confirmation** → BRCA status surrogate only; PARP trials cited but not primary endpoint here
- **Population prevalence estimates** → authors explicitly state large-scale population studies still required

### Curation notes
- Harmonize terminology: paper uses "BRCAness," "HR deficiency," and "BRCA1/BRCA2 deficiency" interchangeably for the HRDetect positive class.
- Flag **RS3 vs rearrangement Signature 3** naming — paper uses RS1–RS6 for rearrangements and COSMIC numbering for SBS.
- Index under both **HRDetect method** (E_Study_Type bridge) and **HRD/mutational signatures** concept (A1).
- Supplementary Tables 13–14 contain normalization means/SDs and final coefficients for implementation.
- Patent disclosure: Davies, Glodzik, Nik-Zainal are inventors — note for reproducibility/licensing.

---

## Related Concepts

HRDetect, BRCAness, homologous recombination deficiency, HRD index, mutational signatures, SBS3, SBS8, Signature 3, Signature 8, rearrangement signature RS3, rearrangement signature RS5, microhomology-mediated indels, lasso logistic regression, glmnet, WGS, WES limitations, biallelic inactivation, loss of heterozygosity, BRCA1 promoter hypermethylation, PARP inhibitor stratification, platinum sensitivity, anthracycline response, neoadjuvant biopsy, TNBC, FFPE sequencing, ASCAT, CaVEMan, Pindel, BRASS, COSMIC signatures, non-negative coefficients, probabilistic classifier, AUC, sensitivity, PARP inhibitor, double-strand break repair

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
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated _(deferred to parent agent)_
- [ ] the corpus `README.md` registry and counts have been updated _(deferred to parent agent)_
