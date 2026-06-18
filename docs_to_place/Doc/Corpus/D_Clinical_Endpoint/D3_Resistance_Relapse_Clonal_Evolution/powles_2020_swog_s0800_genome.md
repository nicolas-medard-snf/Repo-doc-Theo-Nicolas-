---
paper_id: "powles_2020_swog_s0800_genome"
title: "Analysis of Pre- and Posttreatment Tissues from the SWOG S0800 Trial Reveals an Effect of Neoadjuvant Chemotherapy on the Breast Cancer Genome"
authors: "Ryan L Powles, Vikram B Wali, Xiaotong Li, William E Barlow, Zeina A Nahleh, Alastair Thompson, Andrew K Godwin, Christos Hatzis, Lajos Pusztai"
year: 2020
venue: "Clinical Cancer Research"
paper_type: "primary_research"
domain: "D_Clinical_Endpoint"
subdomain: "pre/post-treatment genomic change, residual disease / resistance"
relevance_score: 4
priority_level: "HIGH"
corpus_role: "decision"
temporal_status: "active_candidate"
relevance_tags:
  - "paired_WES"
  - "neoadjuvant_chemotherapy"
  - "SWOG_S0800"
  - "mutational_signature_3"
  - "HRD_BRCA_deficiency"
  - "residual_disease"
  - "VAF_selection"
  - "HFI_mutations"
  - "pathway_level_selection"
  - "non_pCR"
  - "treatment_induced_genomic_change"
doi: "10.1158/1078-0432.CCR-19-2405"
isbn: ""
url: "https://doi.org/10.1158/1078-0432.CCR-19-2405"
pdf_file: "powles_2020_swog_s0800_genome.pdf"
---

## One-Sentence Summary

Using WES of SWOG S0800 pre-treatment biopsies (n=29) and nine paired post-treatment residual-disease samples with >10% tumor cellularity, Powles et al. show that COSMIC signature 3 (BRCA-mediated HRD) predicts pCR, while VAF-rank analysis of paired samples implicates E2F Targets and G2M Checkpoint pathway mutations in chemotherapy-resistant residual clones and depletion of Myogenesis-pathway mutations in clones eradicated by therapy.

---

## Key Contributions

- First large-scale WES effort in a neoadjuvant breast cancer trial comparing pre-treatment mutation landscapes to post-treatment residual disease, using SWOG S0800 FFPE tissues with a pCR-derived pooled "normal cohort" for somatic calling when matched normals were unavailable.
- Links **COSMIC mutational signature 3** (BRCA-mediated homologous recombination deficiency) to higher pCR rate in pre-treatment biopsies (median weight 24% vs 0%, Bonferroni p = 0.007), consistent with prior BRCA/HRD chemosensitivity literature.
- Introduces **VAF percentile-delta rank analysis** across copy-neutral shared mutations to detect treatment selection pressure at variant, gene, and MSigDB hallmark-pathway levels in paired pre/post residual-disease samples.
- Identifies **E2F Targets** (5/9 patients; median percentile delta 80; permutation p = 0.027) and **G2M Checkpoint** (4/9; median percentile delta 80; p = 0.048) pathway HFI mutations enriched in post-treatment residual cancer, and **Myogenesis** pathway HFI mutations depleted (median percentile delta 15; p = 0.021), suggesting clone-specific resistance vs eradication under anthracycline/taxane ± bevacizumab pressure.

---

## Core Idea / Mechanism / Argument

**Central problem.** Single pre-treatment WES snapshots cannot reveal which somatic alterations are selected or depleted when chemotherapy reshapes tumor composition. Paired pre/post analysis is further constrained by post-treatment hypocellularity after effective neoadjuvant therapy.

**Information flow.**

1. **Trial context (S0800, NCT00856492).** Stage II–III breast cancer randomized to three neoadjuvant arms: weekly nab-paclitaxel + bevacizumab → ddAC; nab-paclitaxel → ddAC; or ddAC → nab-paclitaxel. Bevacizumab increased pCR from 21% to 36% (p = 0.019); sequence did not matter in non-bevacizumab arms.

2. **WES cohorts.**
   - **Pre-treatment**: 29 FFPE biopsies (22 residual disease [RD], 7 pCR) from 134 consented patients with pre-treatment tissue.
   - **Paired pre/post**: 9 of 29 with >10% post-treatment tumor cellularity (all RD; no pCR cases in paired set). Median coverage ~174× pre / ~164× post; median 340 / 283 somatic mutations and 54 / 74 HFI mutations per sample.

3. **Variant calling without matched normal.** Seven post-treatment biopsies from pCR patients (no cancer cells) pooled as reference normal for MuTect/Strelka; aggressive germline filtering (dbSNP, ESP6500, 1000G, ExAC; TCGA breast normals; MAF >0.40 filter on shared pre/post variants).

4. **Pre-treatment pCR association.**
   - No individual genes or MSigDB pathways with significantly higher HFI mutation frequency in pCR vs RD after multiple testing.
   - **Signature 3** weight significantly higher in pCR (median 24%, range 0–38%) vs RD (median 0%, range 0–19%; Wilcoxon, Bonferroni p = 0.007). 34% of pre-treatment samples had detectable signature 3.

5. **Paired residual-disease selection analysis.**
   - Shared mutations in copy-neutral regions (SynthEX, K=3) ranked by VAF change pre→post; **percentile delta** captures clone enrichment (high delta) or depletion (low delta) under treatment.
   - Pathway-level: E2F Targets and G2M Checkpoint HFI mutations show significant VAF enrichment in post-treatment residual tissue; Myogenesis HFI mutations show significant depletion—interpreted as eradication of clones harboring those variants.
   - Affected genes vary by patient (e.g., SMC4, TP53, RPA2 in E2F Targets; CDC7, KIF23 in G2M Checkpoint)—pathway convergence without recurrent single-gene drivers.

6. **Claim vs. demonstration.** Signature 3 ↔ pCR link is **demonstrated** in n=29 pre-treatment WES (underpowered for gene-level pCR predictors). Pathway selection in residual disease is **demonstrated** in n=9 paired samples but **not** linked to pCR prediction (paired set is 100% non-pCR by design).

---

## Methodology / Evidence Base

### Empirical design

- **Design**: Prospective-retrospective biomarker analysis within randomized phase II neoadjuvant trial (SWOG S0800); cross-sectional WES for pCR association; longitudinal paired WES for treatment-selection analysis in residual disease.
- **Sample / setting**:
  - Trial accrued 215 patients; 134 with pre-treatment FFPE; 63 post-treatment; 60 paired.
  - WES pre-treatment: **n = 29** (22 RD, 7 pCR).
  - WES paired analysis: **n = 9** (all RD; >10% post-treatment tumor cellularity cutoff per supplementary figure 3).
  - HR+ 20/29 pre-treatment (6/9 paired); HR− 9/29 (3/9 paired). Bevacizumab 14/29 pre (3/9 paired).
- **Intervention / exposure**: Neoadjuvant nab-paclitaxel + dose-dense doxorubicin/cyclophosphamide ± bevacizumab (~20 weeks). Endpoint context mixes **pCR prediction signal** (signature 3, pre-treatment cohort) and **residual-disease / resistance mechanism** (paired VAF selection, n=9).
- **Measurements**: WES (IDT xGen Exome Research Panel v1.0; Illumina HiSeq 4000, 74 bp PE; ~174× median); MuTect v1.1.4 + Strelka v1.0.14; HFI annotation (≥3/5 deleterious predictors or frameshift/stop); deconstructSigs for COSMIC signatures; SynthEX copy-neutral regions; NanoString PanCancer IO 360 for immune metagenes (23 patients with both WES and immune data).
- **Statistical analysis**: Wilcoxon rank-sum (signature weights, mutation counts); Bonferroni correction for signatures; pathway aggregation across 50 MSigDB hallmark sets; VAF percentile-delta with 1000× permutation resampling for pathway-level empirical p-values.
- **Replication**: Single trial substudy; dbGaP phs001883.v1.p1; no external validation cohort for pathway selection calls.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus**: `D_Clinical_Endpoint` → `D3_Resistance_Relapse_Clonal_Evolution`
- **Anchor question(s)**: **AQ-2** (how genomic features differentiate response to neoadjuvant chemotherapy vs other modalities—here, anthracycline/taxane ± bevacizumab selective pressure on clone composition and HRD-linked chemosensitivity) and **AQ-3** (driver vs noise—pathway-level aggregation, HFI filtering, and VAF-rank selection distinguish treatment-enriched vs eradicated alterations; signature 3 as chemosensitivity signal vs E2F/G2M pathway hits as potential resistance context).
- **Bridge corpora**: `A_Genomic_Signal` (A1 HRD/signature 3; A4 drivers: TP53, PIK3CA, SMC4, ERBB3); `B_Therapeutic_Context` (B1 anthracycline/taxane neoadjuvant; B3 bevacizumab arm); `C_Cancer_Subtype` (mixed HR+/HR− stage II–III, not TNBC/HER2+-restricted).

### How it could be used

- **Indirectly inspiring (primary)**: Frames how pre-treatment WES drivers may be **selected against or enriched** in residual disease after neoadjuvant chemotherapy—critical context when interpreting non-pCR WES, even though the project target is pCR prediction.
- **Directly reusable (limited)**: Signature 3 weight as HRD/chemosensitivity covariate for pCR models (supported in pre-treatment n=29); HFI + pathway aggregation logic for deprioritizing sparse single-gene hits; >10% post-treatment cellularity cutoff as QC guardrail for paired analyses.
- **Mainly background / framing**: Paired pre/post WES in residual disease supports **AQ-2/AQ-3 noise filtering**, not direct pCR endpoint prediction (paired n=9 is all non-pCR).

### Main fit with the project

- Demonstrates that **BRCA-related DNA repair deficiency (signature 3)** associates with pCR under standard neoadjuvant chemotherapy—aligns with project's HRD/WES feature class in TNBC/HER2+ contexts, though this cohort is mixed HR status not subtype-stratified.
- Shows **treatment-induced genomic change** is detectable via VAF-rank selection in residual clones (E2F Targets, G2M Checkpoint enriched; Myogenesis depleted)—informs AQ-3 by separating alterations likely representing resistance-enriched signal vs clones lost to therapy.
- Uses WES on FFPE trial tissue with explicit somatic-calling limitations (pCR-pooled normal, no matched germline)—mirrors practical constraints of WES-based gene prioritization pipelines.

### Main mismatch or risk

- **Small n** (29 pre-treatment; **9 paired**, all non-pCR): pathway and signature findings are exploratory; no gene-level pCR predictors survived multiple testing except signature 3.
- **Mixed subtype/regimen**: Includes HR+ and HR−, bevacizumab and non-bevacizumab arms—not cleanly TNBC or HER2+ specific as in project focus.
- **No matched normal DNA**: Aggressive filtering reduces sensitivity; shared pre/post MAF >0.40 filter may remove true somatic events.
- **pCR cases absent from paired analysis** by design (>10% cellularity filter); post-treatment genomic change mechanisms cannot be mapped directly to pCR attainment.

### Concrete follow-up

- Cross-link signature 3 / HRD entries in `A_Genomic_Signal` A1 when ingested; compare effect sizes with GeparSepto and germline BRCA pCR literature cited by authors.
- When building pCR gene lists, treat **E2F Targets / G2M Checkpoint** alterations rising in VAF post-therapy as resistance-context features to deprioritize as pre-treatment pCR predictors unless validated in pre-treatment-only cohorts.
- Pair with `caswelljin_2019_clonal_replacement` for HER2+ multi-region ITH vs this trial's bulk paired WES under cellularity constraints.
- **OCR local PDF** to re-verify all body quotes against co-located source (see Author Notes).

---

## Assumptions

- Pooled pCR post-treatment samples without cancer cells adequately substitute for matched normal in somatic calling (prior work cited: acceptable specificity, reduced sensitivity).
- >10% post-treatment tumor cellularity (supplementary figure 3 cutoff) yields interpretable bulk WES for paired comparison.
- Copy-neutral regions identified by SynthEX (K=3, integer CN 2–3) allow fair VAF comparison despite stromal/treatment-induced cellularity shifts.
- HFI definition (≥3/5 predictors or indel consequence) captures functionally relevant selection targets for pathway aggregation.
- MSigDB hallmark pathway membership adequately aggregates individually rare mutations for treatment-selection inference.
- VAF percentile-delta rank within patient captures clone selection better than absolute VAF given variable cellularity.

---

## Limitations / Failure Modes

- **Severe paired-cohort attrition**: Only 9/29 pre-treatment samples (31%) met post-treatment cellularity threshold—all non-pCR; pCR genomic trajectories not observed post-treatment.
- **No matched normal**: Germline misclassification and lost true somatics despite filtering; MAF >0.40 shared-variant filter likely removes genuine mutations.
- **Small paired n=9**: No recurrent individually selected variants; pathway signals driven by few HFI mutations per pathway (5–8 total across cohort).
- **Mixed HR status and treatment arms**: Bevacizumab effect on genomic selection not isolated; HR+ majority may dilute TNBC-specific signals.
- **FFPE WES**: Archival tissue; no multi-region sampling to disambiguate spatial ITH from true clonal evolution (contrast Caswell-Jin 2019).
- **Endpoint split**: Signature 3 supports pCR context (D1-adjacent) but paired resistance analysis is strictly non-pCR residual disease (D3)—agents must not conflate the two analytic arms.

---

## Key Quantitative or Qualitative Results

| Quantity | Value | Context |
|----------|-------|---------|
| Pre-treatment WES cohort | **n = 29** | 22 RD, 7 pCR |
| Paired pre/post WES | **n = 9** | All RD; >10% post-treatment cellularity |
| Paired cohort as fraction of pre-treatment WES | **9/29 (31%)** | Cellularity cutoff |
| Median somatic mutations (pre / post) | **340 / 283** | Not significantly different post-treatment |
| Median HFI mutations (pre / post) | **54 / 74** | Per sample |
| pCR vs RD mutation count (pre) | **225 vs 354** median | Wilcoxon p = 0.079 (n.s.) |
| Signature 3 weight pCR vs RD | **24% vs 0%** median | Range 0–38% vs 0–19%; Bonferroni p = **0.007** |
| Samples with detectable signature 3 | **34%** | Pre-treatment cohort |
| E2F Targets VAF enrichment (paired) | **5/9** patients; median percentile delta **80** | Permutation p = **0.027** |
| G2M Checkpoint VAF enrichment | **4/9** patients; median percentile delta **80** | Permutation p = **0.048** |
| Myogenesis VAF depletion | median percentile delta **15** | Permutation p = **0.021** |
| Pathways with >60% pre-treatment HFI hit rate | p53, E2F, mTOR, myogenesis, apical junction, mitotic spindle, complement | None enriched for pCR after correction |
| Sequencing depth | **~174×** pre, **~164×** post | 98% bases ≥30× |
| Trial pCR rate (context) | **28%** overall (7/29 in WES cohort) | Bevacizumab 21%→36% in trial |

---

## Key Quotes

> "We performed whole exome sequencing of pre- and post-treatment cancer tissues to assess the somatic mutation landscape of tumors before and after neoadjuvant taxane and anthracycline chemotherapy with or without bevacizumab."

> "29 pre-treatment biopsies from the SWOG S0800 trial were subjected to whole exome sequencing to identify mutational patterns associated with response to neoadjuvant chemotherapy. Nine matching samples with residual cancer after therapy were also analyzed to assess changes in mutational patterns in response to therapy."

> "Contribution of signature 3 to overall mutation signature spectrum was significantly higher in patients who achieved pCR with chemotherapy (median weight 24%, range 0-38% in pCR vs. median weight 0%, range 0-19% in RD, Wilcoxon rank sum, Bonferroni-adjusted p = 0.007)."

> "In our matched cohort, we could identify only 9 of 29 samples with greater than 10% post-treatment tumor cellularity (Supplementary Figure 3), and these were used to compare the tumor genomic landscape before and after therapy."

> "At pathway level, 'E2F Targets' pathway mutations (5/9 patients affected, pathway size: 200 genes) were significantly enriched in post-treatment residual cancer (median percentile delta: 80; permutation p-value: 0.027)."

> "Mutations in 'G2M Checkpoint' pathway (4/9 patients affected, pathway size: 200 genes) also showed a significant VAF enrichment in post-chemotherapy tissues, (median percentile delta: 80; permutation p-value: 0.048)."

> "We also observed a statistically significant VAF depletion of HFI mutations in the 'Myogenesis pathway' in residual cancer suggesting the cell clones harboring these variants were eradicated by chemotherapy (median percentile delta: 15; permutation p-value: 0.021)."

> "These results suggest that genomic disturbances in BRCA-related DNA repair mechanisms, reflected by a dominant mutational signature 3, confer increased chemotherapy sensitivity. Cancers that survive neoadjuvant chemotherapy, frequently have alterations in cell cycle regulating genes but different genes of the same pathways are affected in different patients."

> "Supplementary Figure 3. Pre- and Post-treatment biopsy cellularity for each patient in the SWOG S0800 cohort. The dotted line indicates the selected cut off for retaining samples in pre-post analysis."

> "Supplementary Figure 2. HFI mutations affecting individual recurrent genes in pre-treatment samples. Only genes affected in a minimum of 10% of the cohort are shown."

---

## Cross-References

### Complements entries in corpus
- `caswelljin_2019_clonal_replacement`: Both address neoadjuvant treatment-induced genomic change in breast cancer; Caswell-Jin disambiguates spatial ITH vs clonal replacement with multi-region WES in HER2+ non-pCR, while Powles uses trial-scale bulk paired WES with VAF-rank pathway selection under cellularity constraints.

### Contradicts / Tensions
- **Single-gene pCR predictor studies** (e.g., PIK3CA, TP53 frequency claims): Powles find no individual gene HFI frequency difference between pCR and RD at n=29; only signature 3 and pathway-level paired analysis yield significant signals—tension with over-interpreting sparse WES driver hits for pCR.
- **Low post-treatment cellularity as pure limitation vs selection opportunity**: Authors argue high residual cellularity tumors are "most interesting" for paired comparison but only 9/29 qualify—tension with generalizability to typical hypocellular post-NAC specimens.

### Cross-corpus connections
- **`A_Genomic_Signal` / A1 HRD**: COSMIC signature 3 as BRCA-mediated HRD chemosensitivity marker linked to pCR; connects to HRDetect/HRD-score feature class.
- **`A_Genomic_Signal` / A4 drivers & CNV**: TP53, PIK3CA, SMC4, ERBB3 among pathway-selected HFI hits; no recurrent single-gene pCR association.
- **`B_Therapeutic_Context` / B1 + B3**: Anthracycline/taxane backbone (ddAC + nab-paclitaxel) ± bevacizumab; selection analysis confounded across arms.
- **`C_Cancer_Subtype`**: Mixed HR+/HR− stage II–III; not TNBC- or HER2+-restricted—subtype-specific pCR gene lists require caution.
- **`E_Study_Type`**: Trial FFPE WES with pCR-pooled normal calling strategy; VAF percentile-delta as treatment-selection readout.

### Related entries to add
- **HIGH**: Denkert et al. 2018 GeparSepto signature 3 / pCR (cited comparator).
- **HIGH**: Jiang et al. 2016 BRCA-deficiency transcriptional signature and chemosensitivity in TNBC.
- **MEDIUM**: Shi et al. 2018 reliability of WES ITH (cited for cohort-normal calling).
- **MEDIUM**: Li et al. 2019 SWOG S0800 immune profiling (same trial, immune arm).
- **LOW**: Liedtke et al. 2008 PIK3CA and neoadjuvant response (negative comparator cited).

---

## Author Notes

### Priority justification
**HIGH** (relevance_score 4): One of the first neoadjuvant trial WES studies with paired pre/post tissues in breast cancer; directly addresses treatment-induced genomic change and residual-disease clone selection (D3) while also reporting signature 3 ↔ pCR (supporting AQ-2/AQ-3 gene prioritization under anthracycline/taxane pressure). WES modality matches project data type.

### Use this source for
- Quantifying signature 3 association with pCR under SWOG S0800-like neoadjuvant chemotherapy.
- Understanding VAF percentile-delta / pathway aggregation for detecting treatment-selected HFI mutations in residual disease.
- Setting expectations for paired pre/post WES attrition (>10% cellularity → 9/29 paired).
- Identifying E2F Targets and G2M Checkpoint as resistance-context pathways enriched post-chemotherapy in non-pCR tissue.
- FFPE trial WES somatic-calling constraints when matched normals are absent.

### Do NOT use this source for
- **Definitive TNBC- or HER2+-specific pCR gene lists** → mixed HR cohort, not subtype-stratified.
- **Post-treatment genomic change in pCR patients** → paired analysis excludes pCR (no residual cancer).
- **Single-gene pCR biomarker claims** → no gene-level pCR associations after correction except via signature 3.
- **Bevacizumab-specific genomic selection effects** → not arm-stratified in paired analysis.

### Curation notes
- **Local extraction status**: Co-located PDF (`powles_2020_swog_s0800_genome.pdf`) is a **non-extractable image/raw stream** (FlateDecode; no body text via Read/pdftotext/python). Embedded XMP confirms DOI `10.1158/1078-0432.CCR-19-2405`. Local DOCX parts `_1`, `_2`, `_3` contain **supplementary figure captions only** (not main article text). Body quotes ingested from publisher manuscript matching embedded DOI; **OCR of local PDF recommended** for quote re-verification against co-located file.
- Harmonize **HFI** definition and **signature 3** terminology with A1 HRD entries.
- dbGaP: phs001883.v1.p1.
- Index `VAF percentile-delta`, `pCR-pooled normal WES`, and `SWOG S0800` in cross-reference (suggested below; not edited per ingestion constraints).

---

## Related Concepts

whole exome sequencing (WES); SWOG S0800; neoadjuvant chemotherapy; nab-paclitaxel; dose-dense doxorubicin/cyclophosphamide (ddAC); bevacizumab; pathologic complete response (pCR); residual disease (RD); high functional impact (HFI) mutations; COSMIC mutational signature 3; BRCA-mediated homologous recombination deficiency; HRD; deconstructSigs; MSigDB hallmark pathways; E2F Targets; G2M Checkpoint; Myogenesis pathway; variant allele frequency (VAF); percentile delta; copy-neutral regions; SynthEX; MuTect; Strelka; treatment-induced genomic change; clone selection; chemotherapy resistance; FFPE; tumor cellularity; paired pre/post analysis; pCR-pooled normal reference

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
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated *(deferred per ingestion constraints; suggestions provided to parent agent)*
- [ ] the corpus `README.md` registry and counts have been updated *(deferred per ingestion constraints)*
