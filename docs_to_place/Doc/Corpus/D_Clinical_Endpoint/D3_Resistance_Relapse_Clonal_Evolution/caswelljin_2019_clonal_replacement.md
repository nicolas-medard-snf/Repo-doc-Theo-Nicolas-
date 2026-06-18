---
paper_id: "caswelljin_2019_clonal_replacement"
title: "Clonal replacement and heterogeneity in breast tumors treated with neoadjuvant HER2-targeted therapy"
authors: "Jennifer L. Caswell-Jin, Katherine McNamara, Johannes G. Reiter, Ruping Sun, Zheng Hu, Zhicheng Ma, Jie Ding, Carlos J. Suarez, Susanne Tilk, Akshara Raghavendra, Victoria Forte, Suet-Feung Chin, Helen Bardwell, Elena Provenzano, Carlos Caldas, Julie Lang, Robert West, Debu Tripathy, Michael F. Press, Christina Curtis"
year: 2019
venue: "Nature Communications"
paper_type: "primary_research"
domain: "D_Clinical_Endpoint"
subdomain: "resistance / clonal evolution under neoadjuvant HER2 therapy"
relevance_score: 4
priority_level: "HIGH"
corpus_role: "decision"
temporal_status: "active_candidate"
relevance_tags:
  - "clonal_replacement"
  - "intra_tumor_heterogeneity"
  - "tHFR"
  - "HFR"
  - "neoadjuvant_HER2"
  - "WES_multi_region"
  - "resistant_subclones"
  - "non_pCR_residual_disease"
  - "branching_process_model"
  - "spatial_tumor_growth_model"
doi: "10.1038/s41467-019-08593-4"
isbn: ""
url: "https://doi.org/10.1038/s41467-019-08593-4"
pdf_file: "caswelljin_2019_clonal_replacement.pdf"
---

## One-Sentence Summary

Using multi-region WES and two complementary computational models (spatial agent-based growth and branching-process treatment simulation), Caswell-Jin et al. show that apparent genomic shifts after neoadjuvant HER2-targeted therapy often reflect pre-existing spatial heterogeneity, but that true clonal replacement—with large pre-existing resistant subclones—occurs in a minority of non-pCR HER2+ tumors and implies much higher effective resistance aberration rates than prior estimates.

---

## Key Contributions

- Quantifies spatial intra-tumor heterogeneity (ITH) in 15 untreated primary breast tumors via WES and defines **HFR** (high-frequency regional) and **Fst** as complementary heterogeneity metrics; mean HFR 26% (range 1–70%), higher than colon, brain, lung, and esophageal comparators.
- Applies **tHFR** (temporal HFR)—the proportion of mutations clonal (CCF > 0.5) across all post-treatment regions but absent/rare (CCF < 0.1) pre-treatment—to five HER2+ non-pCR tumors with pre-treatment biopsy WES and 1–5 multi-region post-treatment surgical samples; identifies clonal replacement in 2/5 tumors (P1, P5) while ruling out geographic-killing artifacts via virtual-tumor calibration.
- Integrates **spatial agent-based modeling** (10⁹-cell glandular-fission tumors under selection; ABC inference) and a **continuous-time multi-type branching process** (150-day treatment, effective resistance aberration rate μ) to infer pre-treatment resistant clone sizes (0.02–12.5% of cells), effective μ of 6.0×10⁻⁶–3.4×10⁻⁴ for clonal-replacement cases, and ~10% stochastic rate of clonal replacement across parameter space.

---

## Core Idea / Mechanism / Argument

**Central problem.** Longitudinal WES comparing single pre- and post-treatment samples cannot distinguish true treatment-induced clonal evolution from geographically disparate sampling of a heterogeneous primary tumor. The authors build an analytical framework that explicitly models spatial ITH before interpreting temporal genomic change.

**Information flow.**

1. **Baseline ITH characterization (untreated cohort, n = 15).** Four newly sequenced multi-region FFPE primaries plus 11 from prior multi-region WES/WGS studies. Heterogeneity quantified by:
   - **Fst** (Eq. 1): Hudson estimator on subclonal SNVs (CCF < 0.5), averaging pairwise comparisons across regions—captures post-transformation evolutionary history.
   - **HFR** (Eq. 2): `[R1/(R1+C) + R2/(R2+C)] / 2`, where R1/R2 count mutations with CCF > 0.5 in one region and CCF < 0.1 in the other; C counts mutations clonal in both. Directly measures how often a "clonal" mutation in one biopsy would be reclassified as subclonal in a second region.

2. **Virtual tumor calibration.** Spatial agent-based model simulates 10⁹-cell tumors with glandular fission (deme sizes 1,000–50,000 cells), driver mutation rate 1/10⁵, somatic rate 0.6 mutations/cell division, selection coefficients s = 0–0.5. Demonstrates that with two random biopsies, >25% of apparently clonal mutations in one biopsy can be absent in the other purely from pre-treatment ITH; a second region adds most reclassification value, with diminishing returns beyond two regions.

3. **Treated HER2+ cohort (non-pCR).** Initial n = 20 archival stage II–III HER2+ tumors (neoadjuvant chemotherapy + HER2-targeted therapy, no pCR); after stringent QC (coverage, purity ≥50%, mutation count), **5 tumors** retained adequate post-treatment cellularity for multi-region WES (1 pre-treatment core biopsy + 1–5 spatially distinct post-treatment FFPE blocks + matched normal). ~45% of initial cohort excluded for low post-treatment cellularity.

4. **Clonal-replacement detection via tHFR** (Eq. 3): `tHFR = tR / (tR + tC)`, where tC = mutations with CCF > 0.5 in all post-treatment samples and tR = mutations clonal in all post-treatment samples but CCF < 0.1 pre-treatment. Compared against tHFR distributions from virtual untreated tumors sampled to mimic each patient's scheme:
   - **P1**: tHFR = 0.65 (>99.9th percentile) → clonal evolution, not geographic killing.
   - **P5**: tHFR = 0.30 (>90th percentile; >99th percentile when sampling quadrants matched) → clonal evolution.
   - **P2, P3, P4**: tHFR 0.06–0.12, consistent with pre-treatment heterogeneity alone.
   - At least **two post-treatment regions** were sometimes required to discriminate heterogeneity (P3) from clonal replacement (P5).

5. **Resistant subclone inference.** For P1 and P5, exponential-growth modeling (0.65–2.8%/day) with resistant clone comprising 90–100% of post-treatment tumor yields pre-treatment resistant populations of **0.02–12.5%** of total cells—orders of magnitude larger than the ~10⁻⁶ fraction from EGFR-resistance models in colorectal cancer. Subclonal mutations in P5 pre-treatment (CCF ~0.05) corroborate early emergence of resistance clones. Mutational signature analysis shows subclonal and post-treatment mutations share processes (e.g., mismatch-repair signature in P5), supporting pre-existence rather than treatment-induced mutagenesis.

6. **Branching-process treatment outcomes.** Stochastic model: tumor grows to 10¹⁰ cells (b = 0.15, d = 0.13), then 150-day treatment with sensitive cell death rate d′ ∈ {0.16, 0.20, 0.25} and effective resistance aberration rate μ (product of genomic change rate × number of resistance-conferring sites). Four outcomes: pCR (<10⁴ cells), sensitive residual (≥80% sensitive), clonal replacement (≥80% one resistant clone), polyclonal resistance. Clonal replacement occurs stochastically at ~10% across μ; inferred μ for P1/P5 clonal-replacement with 10–50% tumor shrinkage: **6.0×10⁻⁶ to 3.4×10⁻⁴**, exceeding prior literature estimates (5×10⁻⁸ to 5×10⁻⁶) and implying pCR is impossible at such high μ.

**Claim vs. demonstration.** The framework for disentangling ITH from evolution is **demonstrated** on five deeply sampled non-pCR tumors. Generalization to pCR tumors and to polyclonal vs. sensitive residual disease is **claimed** via modeling but **not directly observed** in WES (low post-treatment cellularity excluded most cases).

---

## Methodology / Evidence Base

### Empirical design

- **Design**: Retrospective observational; multi-region longitudinal WES (pre-treatment biopsy → post-treatment surgical specimen).
- **Sample / setting**:
  - **ITH baseline**: 15 untreated primary breast tumors (6 ER+/HER2−, 2 HER2+, 7 TNBC) with multi-region WES/WGS.
  - **Treated cohort**: 21 HER2+ patients collected (USC); 20 neoadjuvant-treated without pCR; **5** passed QC and had multi-region post-treatment tissue (P1–P5). Treatments: predominantly 6 cycles TCH (docetaxel/carboplatin/trastuzumab); P4 received paclitaxel + neratinib then TCH.
  - **Excluded**: 45% of initial 20-tumor cohort had post-treatment cellularity too low for interpretable bulk WES.
- **Intervention / exposure**: Neoadjuvant HER2-targeted therapy combined with chemotherapy; endpoint context is **residual disease after non-pCR**, not pCR attainment.
- **Measurements**: WES (Agilent SureSelect or Illumina Nextera Rapid Capture Exome); Mutect + VAP variant calling; TitanCNA copy number; CCF via CHAT framework; PyClone clustering; MEDICC copy-number distance; SomaticSignatures/COSMIC signatures.
- **Statistical / computational analysis**: Fst, HFR, tHFR summary statistics; spatial agent-based simulation with ABC parameter inference; continuous-time branching process (100,000 simulations per parameter set); two-sided t-tests for cross-tumor-type comparisons.
- **Replication**: Single-center archival cohort; no external validation cohort for clonal-replacement calls.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus**: `D_Clinical_Endpoint` → `D3_Resistance_Relapse_Clonal_Evolution`
- **Anchor question(s)**: **AQ-2** (how genomic biomarkers differentiate response across therapy types—here, how neoadjuvant anti-HER2 selective pressure reshapes clonal architecture in non-responders) and **AQ-3** (which genes are high-priority drivers vs. background noise—ITH and clonal replacement directly affect whether pre-treatment WES drivers are representative of residual disease).
- **Bridge corpora**: `B_Therapeutic_Context` (B2 anti-HER2: TCH, trastuzumab, neratinib); `C_Cancer_Subtype` (C2 HER2+ stage II–III); `A_Genomic_Signal` (A4 drivers/CNV: PIK3CA, TP53, ERBB2, and candidate resistance alterations in replacement clones).

### How it could be used

- **Indirectly inspiring (primary)**: Provides the mechanistic vocabulary and quantitative bounds for interpreting WES driver lists in neoadjuvant HER2+ settings—especially why single-biopsy drivers may misrepresent post-treatment tumor composition.
- **Directly reusable (limited)**: tHFR/HFR metrics and multi-region sampling logic can inform feature-engineering guardrails (e.g., deprioritizing region-specific subclonal drivers; flagging truncal PIK3CA/TP53 as more stable anchors).
- **Mainly background / framing**: Confirms that resistance/evolution is **supporting context to pCR**, not a pCR prediction endpoint. The study deliberately excludes pCR cases from direct WES assessment.

### Main fit with the project

- Directly relevant to WES-based gene prioritization when the clinical question is neoadjuvant HER2+ response: shows that **pre-treatment biopsy may miss resistance drivers** present at 0.02–12.5% CCF that sweep to clonality after therapy; conversely, apparent genomic "change" may be **spatial sampling artifact** (mean HFR 26–28%).
- Informs AQ-3 noise filtering: PIK3CA and TP53 were clonal across regions when present; 50–75% of other driver/targetable mutations in post-treatment samples were region-specific—supporting deprioritization of single-region subclonal hits.
- Connects effective resistance aberration rate μ to impossibility of pCR at high μ, framing a biological axis (high-μ tumors) distinct from tumors achieving pCR.

### Main mismatch or risk

- **Non-pCR residual-disease cohort only**; ~45% of screened tumors and all pCR cases are not directly sequenced post-treatment. Findings on clonal replacement rates (~2/5 observed; ~10% modeled) cannot be mapped to pCR prediction without extrapolation.
- **Small n = 5** for treated multi-region analysis; HER2+ only; FFPE archival material with purity/coverage filters.
- Does not report pCR-associated driver associations or treatment-response classifiers—evolutionary mechanism paper, not biomarker discovery for pCR.

### Concrete follow-up

- Cross-link resistance-alteration lists from P1/P5 (Supplementary Data) into `A_Genomic_Signal` A4 when those entries exist.
- When ingesting pCR-prediction papers, note whether they used single vs. multi-region pre-treatment sampling; flag driver claims vulnerable to HFR ≥26% reclassification.
- Consider pairing with TNBC neoadjuvant evolution papers (e.g., Kim et al. 2018 scRNA-seq) for subtype-balanced D3 coverage.

---

## Assumptions

- A single pre-treatment core biopsy adequately represents the diagnostic tumor for tHFR numerator/denominator comparisons (authors acknowledge sampling granularity limits).
- CCF thresholds (clonal > 0.5; rare < 0.1) reliably classify mutations despite FFPE artifacts, moderate purity (mean ~62% in breast vs. 78% other types), and ~90× coverage.
- Exponential growth and branching-process parameters (b = 0.15, d = 0.13, 150-day treatment) approximate neoadjuvant HER2+ therapy kinetics.
- Resistant clone comprising 90–100% of post-treatment tumor in P1/P5 (from PyClone) justifies pre-treatment clone-size estimates.
- Spatial agent-based glandular-fission model with deme sizes 1,000–10,000 and s ≥ 0.05 captures breast primary ITH better than neutral evolution (14/15 tumors inconsistent with neutral growth by ABC).
- Bulk WES can detect clonal replacement but cannot distinguish polyclonal resistance from sensitive residual disease without pre-treatment multi-region or single-cell data.

---

## Limitations / Failure Modes

- **Selection bias toward bulky residual disease**: Only tumors with sufficient post-treatment cellularity analyzable; evolutionary trajectories of pCR or near-pCR tumors not directly assessed—modeling only.
- **Low treated-sample n**: Clonal replacement confirmed in 2/5; wide confidence on population frequency.
- **Geographic killing not fully falsifiable in patient tissue**: Ruled out statistically via virtual tumors, but primary tumors were not sampled at octant-level granularity pre-treatment.
- **FFPE and archival quality**: Stringent filters removed 75% of initial treated cohort; results may not generalize to fresh-frozen prospective biopsies.
- **Cannot resolve polyclonal resistance vs. sensitive residual** with current sampling design; branching model predicts polyclonal resistance more common than clonal replacement at high μ.
- **Treatment heterogeneity**: Mostly TCH; one patient (P4) received neratinib—limits uniform B2 bridging.

---

## Key Quantitative or Qualitative Results

| Quantity | Value | Context |
|----------|-------|---------|
| Untreated tumors (multi-region WES) | **n = 15** | 4 new + 11 from literature |
| Initial HER2+ neoadjuvant non-pCR cohort | **n = 20** | Archival USC cohort |
| Multi-region treated analysis | **n = 5** (P1–P5) | After QC; 1–5 post-treatment regions each |
| Post-treatment low cellularity exclusion | **45%** | Of initial 20 |
| Mean HFR (untreated) | **26%** (range 1–70%) | vs. higher than other tumor types (p = 0.015 multivariate) |
| Mean HFR (post-treatment bulky) | **28%** (range 10–54%) | Similar to untreated |
| Clonal replacement observed | **2/5** tumors (P1, P5) | tHFR >90th–99.9th percentile of virtual tumors |
| P1 tHFR | **0.65** | >99.9th percentile |
| P5 tHFR | **0.30** (>99th with quadrant-matched sampling) | Clonal evolution supported |
| P2/P3/P4 tHFR | **0.12 / 0.06 / 0.09** | Consistent with pre-treatment ITH |
| Pre-treatment resistant clone size (P1, P5) | **0.02–12.5%** of cells | vs. ~10⁻⁶ in prior CRC EGFR models |
| Effective resistance aberration rate μ (P1, P5) | **6.0×10⁻⁶ to 3.4×10⁻⁴** | For 10–50% tumor shrinkage + clonal replacement |
| Modeled clonal replacement frequency | **~10%** | Across wide μ and d′ parameter space |
| Region-specific driver/targetable mutations post-treatment | **50–75%** per tumor | Within each of 5 post-treatment tumors |
| Second-region reclassification gain | **~31%** of CCF>0.5 mutations → subclonal with 1 added region | Virtual tumors under selection |
| Two-biopsy ITH artifact | **>25%** of clonal mutations absent in second random biopsy | Pre-treatment breast tumors |

**Treatment outcomes modeled (branching process):** pCR (<10,000 cells); sensitive residual (≥80% sensitive cells); clonal replacement (≥80% one resistant clone); polyclonal resistance. At high μ, pCR impossible; polyclonal resistance more frequent than clonal replacement.

---

## Key Quotes

> "Genomic changes observed across treatment may result from either clonal evolution or geographically disparate sampling of heterogeneous tumors."

> "To assess for clonal replacement, we devise a summary statistic based on whole-exome sequencing of a pre-treatment biopsy and multi-region sampling of the post-treatment surgical specimen and apply this measure to five breast tumors treated with neoadjuvant HER2-targeted therapy."

> "Mean HFR was 26% (range 1–70%), and was significantly higher in breast tumors than other tumor types."

> "In other words, the high level of ITH in breast tumors has substantial implications for understanding changes in tumor composition over time, including with therapy, as geographic genetic differences can mimic genetic divergence observed under clonal evolution."

> "Importantly, while the drastic clonal change across treatment was suggested with only one post-treatment region for P1 (>98th percentile of virtual tumors), multiple regions were needed to discriminate between pre-treatment heterogeneity (P3) or treatment-induced change (P5) for other tumors."

> "Two tumors underwent clonal replacement with treatment, and mathematical modeling indicates these two tumors had resistant subclones prior to treatment and rates of resistance-related genomic changes that were substantially larger than previous estimates."

> "Across a range of feasible growth rates, the resistant subclone was prevalent in the pre-treatment tumor."

> "Notably, these estimates of resistant tumor clone size were substantially larger than those from models in other cancer types predicting ~1 in 1 million cells to be resistant prior to treatment."

> "For these tumors, we inferred effective resistance aberration rates between 6.0 × 10⁻⁶ and 3.4 × 10⁻⁴."

> "Approximately one-half of the tumors we initially profiled pre- and post-treatment were not analyzable with bulk whole-exome sequencing because of low cellularity, consistent with previous work in triple-negative breast cancer."

---

## Cross-References

### Complements entries in corpus
- _(none yet in D_Clinical_Endpoint)_ — this is the first D3 entry; future D1 pCR papers on HER2+ neoadjuvant response should be read alongside this for non-pCR evolutionary counterpoint.

### Contradicts / Tensions
- **Single-sample longitudinal WES studies** (e.g., Balko et al. 2014 TNBC residual disease; Miller et al. 2016 ER+ aromatase inhibition): Caswell-Jin et al. argue many apparent post-treatment genomic shifts may reflect pre-treatment spatial ITH rather than treatment-induced evolution—tension with interpreting driver changes from one pre / one post sample without multi-region post-treatment sampling.
- **Low pre-existing resistance fraction models** (Diaz et al. 2012 CRC EGFR): inferred pre-treatment resistant clones here are 0.02–12.5% of cells, not ~10⁻⁶.

### Cross-corpus connections
- **`B_Therapeutic_Context` / B2 anti-HER2**: TCH backbone; trastuzumab + carboplatin/docetaxel; neratinib in one case—therapy context for interpreting clonal sweeps under HER2 blockade + chemotherapy.
- **`C_Cancer_Subtype` / C2 HER2+**: Stage II–III HER2+ exclusively in treated cohort; ITH baseline includes all subtypes but treated analysis is HER2+-specific.
- **`A_Genomic_Signal` / A4 drivers & CNV**: PIK3CA/TP53 truncal stability; ERBB2 amplifications; candidate resistance alterations in P1/P5 replacement clones (e.g., MYC, ERBB2, PIK3CA, SMARCA4, EGFR—see Supplementary Data); copy-number distance supports clonal replacement in P1/P5 (p = 0.06).
- **`E_Study_Type`**: Exemplar of multi-region WES longitudinal design with computational disambiguation of ITH vs. evolution; QC lessons for low-cellularity post-treatment samples.

### Related entries to add
- **HIGH**: Kim et al. 2018 (Cell) — TNBC chemoresistance single-cell evolution (cited by authors for low cellularity post-treatment).
- **HIGH**: Yates et al. 2015 (Nat Med) — multi-region primary breast ITH foundation.
- **MEDIUM**: Miller et al. 2016 — ER+ neoadjuvant clonal remodeling (contrast subtype).
- **MEDIUM**: Sun et al. 2017 (Nat Genet) — spatial tumor growth model predecessor.
- **LOW**: Diaz et al. 2012 — branching-process resistance baseline for μ comparison.

---

## Author Notes

### Priority justification
**HIGH** (relevance_score 4): Directly addresses how neoadjuvant anti-HER2 therapy reshapes clonal architecture in HER2+ breast cancer—the project's core subtype and treatment axis—using WES, the project's primary data modality. It does not predict pCR but provides essential counter-evidence for interpreting pre-treatment driver lists (AQ-3) and therapy-specific evolution (AQ-2).

### Use this source for
- Explaining why single pre-treatment biopsy drivers may not represent residual post-neoadjuvant tumor.
- Quantifying ITH artifact magnitude (HFR ~26%) when comparing temporal WES samples.
- Understanding tHFR as a clonal-replacement discriminator requiring multi-region post-treatment sampling.
- Parameter bounds on pre-existing resistant subclone sizes and effective resistance aberration rates in HER2+ non-pCR tumors.
- Framing limitations of bulk WES after neoadjuvant therapy when cellularity is low (~45% excluded).

### Do NOT use this source for
- **pCR prediction or pCR-associated driver ranking** → non-pCR residual cohort; pCR cases not directly sequenced.
- **TNBC-specific evolution claims** → treated analysis is HER2+ only (though untreated ITH includes TNBC).
- **Definitive resistance gene list for adjuvant targeting** → candidate alterations in P1/P5 are exploratory; n = 2 clonal-replacement cases.
- **Quantitative pCR rate or response biomarker effect sizes** → endpoint is clonal architecture, not response classification.

### Curation notes
- Harmonize **CCF thresholds** (>0.5 clonal; <0.1 rare) with other PyClone-based corpus entries.
- **tHFR** and **HFR** should be indexed as named summary statistics in `CROSS_REFERENCE_INDEX.md` (suggested additions below—not edited per ingestion constraints).
- Supplementary Data contains per-patient mutation/cluster tables and resistance-alteration annotations (Cancer Genome Interpreter)—high value for A4 cross-walk when ingested.
- EGA accession EGAD00001004306 for raw WES data.
- Code: https://github.com/cancersysbio/BreastCancerITH

---

## Related Concepts

intra-tumor heterogeneity (ITH); spatial heterogeneity; clonal replacement; clonal evolution; geographic killing; HFR (high-frequency regional); tHFR (temporal HFR); Fst; cancer cell fraction (CCF); multi-region whole-exome sequencing; neoadjuvant therapy; HER2-positive breast cancer; non-pCR residual disease; resistant subclone; effective resistance aberration rate; branching process; agent-based spatial tumor model; Approximate Bayesian Computation (ABC); PyClone; pathologic complete response (pCR, as contrast endpoint); polyclonal resistance; driver mutation; subclonal mutation; truncal mutation; FFPE WES; TCH regimen; trastuzumab

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
