---
paper_id: "kim_2025_wgs_breast_landscape"
title: "Whole-genome landscapes of 1,364 breast cancers"
authors: "Ryul Kim, Jonghan Yu, Joonoh Lim, Brian Baek-Lok Oh, Seok Jin Nam, Seok Won Kim, Jeong Eon Lee, Byung Joo Chae, Ji-Yeon Kim, Ga Eun Park, Bong Joo Kang, Pill Sun Paik, Soo Yeon Bae, Chang Ik Yoon, Young Joo Lee, Dooreh Kim, Kabsoo Shin, Ji Eun Lee, Jun Kang, Ahwon Lee, Erin Connolly-Strong, Sangmoon Lee, Bo Rahm Lee, Yuna Lee, Ki Jong Yi, Young Oh Kwon, In Hwan Chun, Junggil Park, Jihye Kim, Chahyun Choi, Jong Yeon Shin, Hyungjung Lee, Minji Kim, Hansol Park, Ilecheon Jeong, Boram Yi, Won-Chul Lee, Jeong Seok Lee, Woo Chan Park, Sung Hun Kim, Yoon-La Choi, Jeongmin Lee, Young Seok Ju, Yeon Hee Park"
year: 2025
venue: "Nature"
paper_type: "primary_research"
domain: "E_Study_Type"
subdomain: "whole-genome breast cancer cohort / driver & signature landscape"
relevance_score: 5
priority_level: "CRITICAL"
corpus_role: "decision"
temporal_status: "active_candidate"
relevance_tags:
  - "WGS"
  - "CUBRICS_cohort"
  - "driver_genes"
  - "mutational_signatures"
  - "HRD"
  - "TMB"
  - "structural_variants"
  - "ecDNA"
  - "neoadjuvant_TCHP"
  - "pCR"
  - "HER2_positive"
  - "TNBC"
  - "MATH_heterogeneity"
  - "CancerVision"
doi: "10.1038/s41586-025-09812-3"
isbn: ""
url: "https://doi.org/10.1038/s41586-025-09812-3"
pdf_file: "kim_2025_wgs_breast_landscape.pdf"
---

## One-Sentence Summary

Kim et al. report the CUBRICS cohort — 1,364 clinically annotated Korean breast cancer WGS (plus transcriptome for 88.6%) — cataloguing 41 IntOGen driver genes, SNV/indel/SV mutational signatures, HRD/TMB/MATH pattern biomarkers, and a neoadjuvant TCHP HER2+ pCR substudy (n = 75), providing the project's largest WGS-scale driver and signature reference for breast cancer.

---

## Key Contributions

- **Largest clinically integrated breast WGS cohort to date (CUBRICS)**: 1,364 tumour–normal WGS pairs from Samsung Medical Center and Seoul St Mary's Hospital (2012–2023), median age 44 years, with whole-transcriptome data for 1,209 cases (88.6%) enabling PAM50 and IntClust subtyping.
- **Pan-genome mutation catalogue**: 10,929,118 somatic mutations (8,935,132 SNVs; 1,785,446 indels; 208,540 SVs); IntOGen consensus identifies **41 protein-coding driver genes** including four putative novel drivers (BCL11B, RREB1, RAF1, SPECC1).
- **Signature and pattern biomarker landscape**: 17 SNV, 9 indel, and 6 SV signatures; bimodal HRD scoring (315/1,364 = 23.1% HRD); subtype-specific TMB; MATH heterogeneity linked to survival and anti-HER2 PFS.
- **Structural and copy-number architecture**: SV interaction maps, recurrent fusions (e.g., NRG1 in 110 cases), ecDNA in 387 tumours (28.4%), focal amplifications (ERBB2 18.7%, CCND1 7.9%, ZNF703 9.1%, FGFR1 7.8%), and CNA timing suggesting early genomic instability decades before diagnosis.
- **Clinicogenomic treatment associations**: TNBC adjuvant anthracycline–cyclophosphamide DFS by HRD status (n = 89); **neoadjuvant TCHP pCR analysis in 75 HER2+ tumours** (38 pCR / 37 non-pCR) with ERBB2 copy number, chromothripsis, and PIK3CA associations; CDK4/6i and anti-HER2 metastatic PFS biomarkers (MATH, TMB, HRD).

---

## Core Idea / Mechanism / Argument

**Central problem.** Targeted sequencing and partial genomic views miss rearrangements, copy-number architecture, signature-level processes, and clinically annotated WGS-scale integration. The authors argue that tumour–normal WGS paired with full medical records is necessary to link pattern-driven genomic features to treatment outcomes.

**Information flow.**

1. **Cohort assembly (CUBRICS).** Prospective and retrospective Korean breast cancers with archived tumour and matched blood; CancerVision CLIA WGS (NovaSeq 6000; ~40× tumour, ~20× normal) and RNA-seq for most cases. Younger, less ER+/luminal A than Western cohorts.

2. **Driver discovery.** Seven IntOGen algorithms (dNdScv, OncodriveFML, OncodriveCLUSTL, cBaSE, MutPanning, HotMAPS, smRegions) combined via weighted Stouffer voting → 41 drivers after manual curation (q < 0.10). Classical drivers (TP53, PIK3CA, GATA3) plus novel candidates with subtype and IntClust context.

3. **Mutational processes.** Constrained non-negative least squares signature fitting (COSMIC reference signatures) yields SNV/indel/SV signature exposures. HRD score integrates SBS3/SBS8, ID6, RS3/RS5, microhomology deletions, and CNV features → bimodal HRD/HRP classification with germline/somatic HR-pathway annotation.

4. **Structural variation and amplification.** Delly SV calls; 5-Mb interaction maps; super-enhancer proximity to ERBB2 extragenic SVs (enhancer hijacking hypothesis); AmpliconArchitect ecDNA detection; GISTIC recurrent CNAs; F-score for focal amplifications.

5. **Timing and resistance.** Molecular-time π for CNA acquisition; long-segment CNAs often by 20% molecular time (decades pre-diagnosis); late CNA acceleration in HRD; illustrative BRCA1 frame-restoring indel reverting HRD→HRP under talazoparib.

6. **Clinical integration.** Pattern scores (HRD, TMB, MATH) associated with adjuvant chemo DFS (TNBC), neoadjuvant TCHP pCR (HER2+), and first-line metastatic anti-HER2 or CDK4/6i PFS — framed as hypothesis-generating pending prospective validation.

**Claim vs. demonstration.** The **genomic landscape and driver/signature catalogue** are **demonstrated** at scale. **Predictive biomarker utility** for specific regimens is **claimed** with internal cohort statistics and some external validation (e.g., TransNEO for ERBB2 CN–pCR), but authors emphasize need for prospective trials and note left-truncation/survival bias limitations.

---

## Methodology / Evidence Base

### Empirical design

- **Design**: Observational clinicogenomic cohort (mixed prospective/retrospective); substudy components linked to trials NCT03131089 and NCT06334471.
- **Sample / setting**: **N = 1,364** breast cancers (Korean CUBRICS); **n = 1,209** with WTS (88.6%); PAM50 subtypes luminal A/B, HER2-enriched, basal-like, normal-like.
- **Intervention / exposure (substudies)**: Adjuvant anthracycline–cyclophosphamide in TNBC (n = 89 for HRD–DFS); neoadjuvant **TCHP** (docetaxel, carboplatin, trastuzumab, pertuzumab) in HER2+ (n = 75); first-line palliative anti-HER2 (n = 45) and CDK4/6i + endocrine (n = 57).
- **Measurements**: CancerVision WGS pipeline — bwa-mem, Mutect2/Strelka2, Sequenza purity/ploidy/CNV, Delly SV, GISTIC, AmpliconArchitect ecDNA, IntOGen drivers, proprietary HRD score, MATH from WGS, PAM50 (genefu), IntClust (ic10).
- **Statistical analysis**: Kaplan–Meier, Cox proportional hazards (multivariate with covariates), Fisher/chi-square/t-tests per figure legends; signature fitting via pracma active-set NNLS.
- **Replication**: External validation cited for MATH (METABRIC), ERBB2 CN–pCR (TransNEO), 9q23 OS (METABRIC); no full-cohort external replication of all biomarker claims.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus**: `E_Study_Type` → `E4_Genomic_Cohort_Landscape`
- **Anchor question(s)**: **AQ-1** (WES/WGS-derived drivers — here WGS-scale driver catalogue and neoadjuvant pCR-associated mutations in HER2+ TCHP) and **AQ-3** (high-priority driver vs. background noise — 41 IntOGen drivers, PIK3CA enrichment in non-pCR, truncal vs. subclonal framing via CCF/MATH).
- **Bridge corpora**: `A_Genomic_Signal` — A1 HRD/signatures (SBS3, HRD score, 315 HRD cases); A4 drivers/CNV/SV (TP53, PIK3CA, ERBB2 ecDNA/CN, RB1/PTEN/RUNX1 SV truncations); A5 chromatin (BCL11B); `E6_Sequencing_Platform` (CancerVision WGS assay, NovaSeq, GRCh38); `D_Clinical_Endpoint` (neoadjuvant pCR n = 75 HER2+); `C_Cancer_Subtype` (PAM50-stratified findings); `B_Therapeutic_Context` (TCHP anti-HER2, platinum in TCHP, CDK4/6i).

### How it could be used

- **Directly reusable**: Canonical breast driver list (41 genes); HRD prevalence by subtype; signature reference set; ERBB2 CN threshold (≥33) and chromothripsis as pCR stratifiers in neoadjuvant TCHP; PIK3CA as non-pCR enrichment — all map to WES/WGS feature engineering for TNBC/HER2+ neoadjuvant response.
- **Indirectly inspiring**: WGS-vs-WES gap analysis (SVs, ecDNA, enhancer hijacking invisible to WES); Korean cohort age/subtype composition vs. Western training sets.
- **Mainly background / framing**: Adjuvant and metastatic PFS endpoints; etiology/timing of CNAs; germline APOBEC3A/B deletion epidemiology.

### Main fit with the project

- Project overview explicitly lists the **WGS landscape** as a core asset; this is the authoritative large-scale breast WGS cohort with **neoadjuvant pCR data** (75 HER2+ TCHP) directly aligned with TNBC/HER2+ pCR prediction goals.
- Supplies method-compatible upstream context for WES projects: driver priors, HRD/TMB/MATH pattern features, and noise-vs-signal framing (e.g., PIK3CA in non-pCR; ERBB2 expression/CN in pCR).

### Main mismatch or risk

- **WGS not WES**: Project primary data axis is WES; SV-heavy biology, ecDNA, and enhancer-hijacking ERBB2 activation may be under-detected on exome — do not assume feature parity.
- **Korean cohort skew**: Younger median age (44), lower ER+/luminal A; HRD/APOBEC3A/B allele frequencies differ from European cohorts.
- **Mixed endpoints**: Many findings are adjuvant DFS, metastatic PFS, or OS — not neoadjuvant pCR; only HER2+ TCHP substudy (n = 75) is directly pCR-relevant.
- **Local PDF text not machine-verified** at ingestion (see Limitations); quotes below sourced from publisher HTML at DOI.

### Concrete follow-up

- Bridge driver list and HRD/TMB thresholds into `A_Genomic_Signal` A1/A4 entries; cross-link `davies_2017_hrdetect` and `telli_2016_hrd_score` for HRD method comparison.
- Extract Supplementary Tables (driver list, signature exposures, TCHP clinicogenomic grid) when PDF OCR/local extraction is available.
- Flag PIK3CA, luminal subtype, hormone receptor positivity as non-pCR correlates when scoring HER2+ neoadjuvant models.

---

## Assumptions

- Tumour–normal WGS at ~40×/20× with CancerVision curation captures clinically relevant drivers and SVs in FFPE/fresh-frozen mix.
- IntOGen seven-method consensus with COSMIC CGC weighting and manual curation yields a stable 41-gene driver set generalizable to other breast WES/WGS pipelines.
- Proprietary HRD score (signature + CNV composite) is comparable to HRDetect/HRD-score literature tools for ranking HRD-enriched TNBC.
- Pre-treatment samples for survival and neoadjuvant substudies were collected before targeted therapy-induced genome reshaping (stated for survival analyses).
- PAM50 from WTS and IHC-based HER2 status are adequate for subtype-stratified driver and pCR analyses despite known HER2 IHC/WGS discordance cases illustrated in Fig. 4d.

---

## Limitations / Failure Modes

- **Ingestion constraint**: Local PDF text extraction failed (pdftotext unavailable; Python/pypdf/pdfplumber unavailable on ingestion host). Bibliographic metadata extracted from PDF XMP; body content verified against Nature publisher HTML at DOI — **local PDF text layer not independently verified; OCR/re-extraction recommended** before treating co-located PDF as quote source.
- **Left-truncation / immortality bias**: Mixed retrospective/prospective enrolment may inflate survival estimates; authors urge caution especially for de novo metastatic subgroup.
- **Hypothesis-generating clinicogenomics**: Many treatment–biomarker associations lack prospective trial validation; multiple comparisons not always adjusted.
- **WGS→WES transfer risk**: ecDNA (28.4%), distal SVs, and enhancer hijacking may be missed on exome-only project datasets.
- **Population specificity**: Korean CUBRICS demographics limit direct transfer to Western neoadjuvant trial cohorts without recalibration.

---

## Key Quantitative or Qualitative Results

| Quantity | Value | Context |
|----------|-------|---------|
| WGS cohort (CUBRICS) | **N = 1,364** | Korean; median age 44 years |
| WTS available | **n = 1,209** (88.6%) | PAM50 subtyping |
| Total somatic mutations | **10,929,118** | 8,935,132 SNVs; 1,785,446 indels; 208,540 SVs |
| IntOGen driver genes | **41** | 4 putative novel (BCL11B, RREB1, RAF1, SPECC1) |
| Median TMB (all) | **4,742** (IQR 2,392–8,842) | Basal-like highest: 8,360 |
| HRD cases | **315/1,364 (23.1%)** | Basal-like 182/252 (72.2%) |
| HR-pathway causal variants in HRD | **130/315 (41.3%)** | 90 germline; 40 somatic-only |
| SV events | **208,540** | 78.2% local intrachromosomal (<5 Mb) |
| ecDNA-positive tumours | **387/1,364 (28.4%)** | Correlated with F-score peaks |
| ERBB2 focal amplification | **255/1,364 (18.7%)** | chr. 17 peak |
| TNBC adjuvant chemo HRD vs HRP DFS | **HR 0.10** (95% CI 0.02–0.54; P = 0.006) | n = 89; HRD n = 66 |
| HER2+ neoadjuvant TCHP | **n = 75** | **38 pCR / 37 non-pCR** |
| PIK3CA in non-pCR vs pCR | **P = 0.003** | Fisher's exact |
| ERBB2 CN ≥33 pCR precision | **30/38 (78.9%)** | vs HER2 IHC 3+ sensitivity 36/38 (94.7%) |
| Chromothripsis in pCR vs non-pCR | **71.1% vs 43.2%** | chi-square |
| MATH ≥40 vs PFS (anti-HER2 1L) | **HR 2.95** (95% CI 1.48–5.91; P = 0.002) | n = 45 |

---

## Key Quotes

> "Here, to comprehensively characterize its genomic landscape and the clinical significance of genomic characteristics, we analysed whole-genome sequences from 1,364 clinically annotated breast cancers, with transcriptome data available for most cases."

> "To our knowledge, this cohort—referred to as CUBRICS cohort—is the largest of its kind to date."

> "From the 1,364 whole-genome sequences, we identified 10,929,118 somatic mutations, which include 8,935,132 single nucleotide variants (SNVs), 1,785,446 indels and 208,540 structural variants with a substantial variation in their burden per sample."

> "By applying the IntOGen pipeline, we identified 41 breast cancer driver genes (Methods), including 4 novel driver genes in addition to classical drivers such as TP53, PIK3CA and GATA3."

> "The combined estimated HRD scores showed a clear bimodal distribution, identifying 315 cases as HRD in the CUBRICS cohort (23.1%, 315 out of 1,364)."

> "Out of 75 individuals with HER2-positive tumours who received neoadjuvant TCHP regimens, 38 showed pathologic complete response (pCR)."

> "Although cases without pCR (n = 37) were characterized by a higher prevalence of luminal subtypes, hormone receptor positivity and PIK3CA mutations, cases with pCR (n = 38) exhibited significantly higher ERBB2 expression and a greater frequency of ERBB2 focal amplification."

> "Although HER2 IHC 3+ was a sensitive biomarker for pCR (36 out of 38, 94.7%), ERBB2 copy number (n ≥ 33) demonstrated higher precision (30 out of 38, 78.9%)."

> "Further, we observed a significant enrichment of chromothripsis events in cases with pCR (71.1% versus 43.2%)."

> "Overall, this study enhances our understanding of the genomic landscape of breast cancer and underscores the value of WGS in discovery research and its potential to inform future clinical strategies, contingent upon further validation."

---

## Cross-References

### Complements entries in corpus
- `davies_2017_hrdetect` / `telli_2016_hrd_score` (A1): independent HRD scoring methods to compare against CUBRICS proprietary HRD score and 315-case HRD prevalence.
- `caswelljin_2019_clonal_replacement` (D3): complementary HER2+ neoadjuvant genomics — Caswell-Jin focuses on multi-region WES clonal replacement in non-pCR; Kim et al. provide bulk WGS pCR stratifiers (ERBB2 CN, chromothripsis, PIK3CA).
- `sammut_2022_multiomic_ml` (A6): multi-omic ML for response — Kim et al. supply raw feature catalogue (drivers, signatures, CN/SV) that such models could consume.

### Contradicts / Tensions
- **HRD as biomarker is context-dependent**: HRD predicts **better** adjuvant chemo DFS in TNBC (Fig. 2f) but **worse** CDK4/6i PFS in HR+/HER2− metastatic setting (Fig. 5f,g) — must not treat HRD as uniformly "good" or "bad" without B- and C-axis conditioning.

### Cross-corpus connections
- **A_Genomic_Signal / A1**: SBS3/SBS8/ID6/SV3/SV5 HRD signatures; 17 SNV + 9 indel + 6 SV signature compendium.
- **A_Genomic_Signal / A4**: 41 drivers; ERBB2 ecDNA/CN; RB1/PTEN/RUNX1 SV truncations; NRG1 fusions.
- **E6_Sequencing_Platform**: CancerVision CLIA WGS (NovaSeq 6000, GRCh38, Mutect2/Strelka2/Delly/Sequenza stack).
- **D_Clinical_Endpoint**: Neoadjuvant TCHP pCR n = 75 — direct pCR endpoint evidence for HER2+.
- **C_Cancer_Subtype**: PAM50-stratified TMB, HRD, drivers.
- **B_Therapeutic_Context**: TCHP (B2 anti-HER2 + platinum); CDK4/6i (B1 endocrine axis).

### Related entries to add
- **HIGH**: TransNEO external validation cohort paper (ERBB2 CN–pCR); METABRIC references for MATH/9q23 validation.
- **MEDIUM**: CancerVision assay methods paper (ref. 58); IntOGen 2023 pipeline documentation.
- **LOW**: Individual novel driver functional papers (BCL11B, RREB1).

---

## Author Notes

### Priority justification
- **CRITICAL** for the project: largest clinically annotated breast WGS landscape; directly supplies driver catalogue, signature/HRD/TMB reference distributions, and neoadjuvant HER2+ pCR genomic correlates — the upstream evidence base the project overview names as a core asset.

### Use this source for
- Breast cancer driver gene prior list (41 IntOGen genes) for AQ-3 noise filtering
- HRD prevalence and HR-pathway defect breakdown by PAM50 subtype
- Mutational signature reference (17 SNV / 9 indel / 6 SV) for WGS/WES signature feature design
- Neoadjuvant TCHP pCR correlates: ERBB2 CN ≥33, chromothripsis, PIK3CA, luminal/HR+ enrichment in non-pCR
- WGS platform and pipeline provenance (CancerVision / E6 bridge)
- SV/ecDNA/CNA timing biology as background for WES coverage gaps

### Do NOT use this source for
- Direct WES feature parity claims without checking capture limits → use WES-specific cohort papers
- Universal HRD treatment recommendation → HRD effect direction differs by regimen (adjuvant chemo vs CDK4/6i)
- Population-general prevalence without Korean-cohort caveat
- Verbatim quotes from co-located PDF until local text extraction/OCR confirms text layer

### Curation notes
- **OCR / local PDF re-extraction recommended**: ingestion host lacked pdftotext and Python; quotes verified against Nature HTML at https://doi.org/10.1038/s41586-025-09812-3, not local PDF text layer.
- Harmonize HRD terminology: proprietary composite score vs HRDetect vs scarHRD vs HRD-score literature.
- Interactive explorer: https://open.cancervision.com
- Update `E_Study_Type/CROSS_REFERENCE_INDEX.md` (hub entry candidate) and README registry when permitted.

---

## Related Concepts

CUBRICS, whole-genome sequencing, IntOGen, driver genes, mutational signatures, COSMIC SBS, HRD, HRP, TMB, MATH, structural variation, ecDNA, chromothripsis, enhancer hijacking, gene fusions, NRG1, ERBB2 amplification, neoadjuvant TCHP, pathologic complete response, PAM50, IntClust, CancerVision, molecular timing, copy number alteration, APOBEC3A/B, PIK3CA, TP53, Korean breast cancer cohort

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
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated (deferred per ingestion task constraints)
- [ ] the corpus `README.md` registry and counts have been updated (deferred per ingestion task constraints)
- [x] the summary is useful for this project, not just generally informative
