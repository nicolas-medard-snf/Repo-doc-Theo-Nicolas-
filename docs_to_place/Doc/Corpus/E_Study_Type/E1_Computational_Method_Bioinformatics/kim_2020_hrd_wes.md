---
paper_id: "kim_2020_hrd_wes"
title: "Determining homologous recombination deficiency scores with whole exome sequencing and their association with responses to neoadjuvant chemotherapy in breast cancer"
authors: "Seung Jin Kim, Yoshiaki Sota, Yasuto Naoi, Keiichiro Honma, Naofumi Kagara, Tomohiro Miyake, Masafumi Shimoda, Tomonori Tanei, Shigeto Seno, Hideo Matsuda, Shinzaburo Noguchi, Kenzo Shimazu"
year: 2020
venue: "Translational Oncology"
paper_type: "primary_research"
domain: "E_Study_Type"
subdomain: "HRD scoring from WES (bioinformatics method)"
relevance_score: 4
priority_level: "HIGH"
corpus_role: "reference"
temporal_status: "active_candidate"
relevance_tags:
  - "HRD_score"
  - "WES"
  - "scarHRD"
  - "Sequenza"
  - "LOH"
  - "TAI"
  - "LST"
  - "NtAI"
  - "neoadjuvant"
  - "pCR"
  - "breast_cancer"
  - "HRR_genes"
  - "OncoScan"
  - "PureCN"
doi: "10.1016/j.tranon.2020.100986"
isbn: ""
url: "https://doi.org/10.1016/j.tranon.2020.100986"
pdf_file: "kim_2020_hrd_wes.pdf"
---

## One-Sentence Summary

Kim et al. (2020) apply WES-based genomic-scar HRD scoring (LOH/TAI/LST via Sequenza and scarHRD) in a neoadjuvant breast cancer cohort and relate HRD-high status to clinicopathologic features and chemotherapy response — a directly relevant E1 bridge for computing the project's HRD signal from WES rather than SNP-array platforms, pending full OCR of the co-located PDF.

---

## Key Contributions

- **Claimed (bibliographic record; body not yet OCR'd from co-located PDF):** Demonstrates that WES can be used to derive HRD scores comparable to SNP-array/OncoScan approaches in breast cancer.
- **Claimed:** Applies standard scar-based HRD scoring (sum of LOH, TAI, LST with HRD-high threshold ≥42) on pretreatment tumor WES with matched germline, in a neoadjuvant chemotherapy setting (paclitaxel followed by FEC; subset with trastuzumab in HER2+).
- **Claimed:** Relates WES-derived HRD status to HRR gene mutation class (germline vs somatic vs wild-type) and to pathologic response endpoints (pCR, near-pCR) across breast cancer subtypes including luminal disease.
- **Methodological value for this project:** Documents a concrete WES → copy-number → scarHRD pipeline compatible with the project's WES-first data modality, complementing array-validated methods in `telli_2016_hrd_score` and NGS migration work (Sztupinszki et al., scarHRD).

---

## Core Idea / Mechanism / Argument

### What this source is (from title + domain context)

This is a **primary clinical–bioinformatics study** at the intersection of **E1 (computational method)** and **E6 (WES platform)**: it operationalizes the established **genomic-scar HRD score** on **whole exome sequencing** data rather than on the original SNP-array assay used to define the score in prior validation work.

### HRD score mechanism (inherited from prior literature; not re-derived in this entry)

The HRD score used in the scarHRD ecosystem is the **unweighted sum of three chromosomal instability scars** reflecting homologous recombination repair deficiency:

- **HRD-LOH** (loss of heterozygosity scar)
- **TAI / NtAI** (telomeric allelic imbalance)
- **LST** (large-scale state transitions)

Tumors with total score **≥42** are commonly classified **HRD-high** (threshold from the Myriad/Telli training framework; see `telli_2016_hrd_score` in A1).

### WES computation pipeline (domain-standard; specific tool versions pending OCR)

For WES data, the standard scarHRD workflow requires **allele-specific copy number** from paired tumor–normal sequencing before scar counting:

1. WES alignment and variant calling (typical GATK/BWA stack on GRCh38).
2. Copy-number / purity estimation (commonly **Sequenza** or ASCAT-class tools).
3. **scarHRD** R package on segmentation output to compute LOH, TAI, LST and their sum.

The paper title and venue metadata indicate the authors **validate WES-derived HRD against array-based OncoScan** in a subset and then analyze **neoadjuvant response** — positioning the work as both a **platform migration study** and a **clinical biomarker application**, not a new scar definition.

### Claimed vs demonstrated (pending body verification)

| Aspect | Status |
|--------|--------|
| Bibliographic identity (authors, year, venue, DOI) | Verified from PubMed/PMC record |
| WES HRD pipeline details (versions, parameters, QC cutoffs) | **Pending OCR** from co-located PDF |
| WES vs array concordance statistics | **Pending OCR** |
| pCR / near-pCR association effect sizes | **Pending OCR** |
| Direct quotes | **Pending OCR** |

---

## Methodology / Evidence Base

### If methodological / applied / "how-to" (partial — pending OCR)

- **What the method does:** Derives scar-based HRD scores from WES copy-number profiles using the Sequenza → scarHRD stack; compares to OncoScan/ASCAT-derived scores; classifies HRD-high at threshold ≥42; co-analyzes HRR gene germline/somatic mutation status.
- **What it requires (inputs):** Paired tumor–normal WES (pretreatment biopsy); BAM/VCF inputs for copy-number callers; scarHRD R package; reference genome (GRCh38 per external record).
- **Where used in practice:** Neoadjuvant breast cancer cohort (Osaka University; stages II–III, one stage IV) treated with paclitaxel → FEC (± trastuzumab in HER2+); response graded by Japanese Breast Cancer Society pathologic criteria (pCR and near-pCR).

### Empirical design (high-level; from title + external bibliographic record)

- **Design:** Retrospective observational cohort with pretreatment WES.
- **Sample / setting:** n ≈ 120 breast cancer patients (exact inclusion/exclusion pending OCR).
- **Intervention / exposure:** Neoadjuvant paclitaxel + FEC (non-platinum anthracycline/taxane regimen); not a platinum/PARP trial.
- **Measurements:** WES HRD score; HRR gene mutation panel; IHC/FISH subtyping; pathologic response.
- **Statistical analysis:** Correlation (WES vs array); subtype comparisons; logistic regression for response (details pending OCR).

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus:** `E_Study_Type` → `E1_Computational_Method_Bioinformatics`
- **Anchor question(s):** **AQ-1** (WES-derived genomic features correlated with pCR — HRD is a composite WES-extractable signal); **AQ-3** (method-grade evidence for prioritizing HRD/HRR-related biology vs noise — distinguishes germline HRR mutation, somatic HRR mutation, and scar-only HRD-high status).
- **Bridge corpora:**
  - **`A_Genomic_Signal` / A1** — defines how the HRD genomic signal is computed from WES for downstream gene/feature tagging.
  - **`E6_Sequencing_Platform`** — WES assay, coverage, and copy-number feasibility on pretreatment biopsies.

### How it could be used

- **Directly reusable (after OCR upgrade to decision):** WES → Sequenza → scarHRD pipeline specification; HRD-high threshold; WES–array concordance benchmarks; pretreatment biopsy feasibility parameters.
- **Indirectly inspiring:** Example of applying scarHRD on non-platinum neoadjuvant regimens (P-FEC), relevant when project's TNBC/HER2+ cohorts are not uniformly platinum-treated.
- **Mainly background / framing:** Confirms WES as a viable HRD platform alongside SNP arrays — supports the project's WES-first assumption pending full method extraction.

### Main fit with the project

The project relies on **WES** to surface treatment-predictive genomic signals. This paper sits at the **upstream E-layer**: it specifies *how* to compute HRD from WES — the same signal class prioritized in A1 and referenced in multi-omic benchmarks (`sammut_2022_multiomic_ml`). Neoadjuvant setting and pCR/near-pCR endpoints align with the project's clinical target, though regimens differ from uniform platinum or modern HER2-targeted trial designs.

### Main mismatch or risk

- **Regimen mismatch:** Primary analysis emphasizes **non-platinum** P-FEC; platinum-sensitive HRD biology may not transfer directly to anthracycline/taxane response interpretation.
- **Subtype emphasis:** External abstract highlights luminal-subtype near-pCR association; project's core subtypes are **TNBC and HER2+** — subtype-specific claims require OCR verification before weighting.
- **Reference-grade ingestion:** Without OCR of the co-located PDF, method parameters, QC exclusions, and effect sizes cannot be cited as decision-grade evidence.
- **Not HRDetect:** Uses **scar sum (LOH+TAI+LST)**, not the multi-signature HRDetect classifier in `davies_2017_hrdetect` — different HRD operationalization with known WES trade-offs.

### Concrete follow-up

1. **OCR the co-located PDF** and upgrade `corpus_role` to `decision` with verified quotes, tool versions, and effect sizes.
2. Cross-link to `telli_2016_hrd_score` (threshold ≥42 provenance) and Sztupinszki/scarHRD (NGS migration reference cited by this paper).
3. Map pipeline outputs to project's WES feature-extraction checklist (PureCN vs Sequenza choices, minimum cellularity, coverage).
4. Evaluate whether luminal-subtype findings should be tagged out-of-scope per project boundaries or retained as methodological validation only.

---

## Assumptions

- Scar-based HRD (LOH + TAI + LST, threshold ≥42) adequately proxies HR pathway deficiency on WES-derived copy number — inherited from prior Myriad/scarHRD literature, not independently re-proven in this entry.
- Pretreatment core biopsy WES with sufficient tumor cellularity yields copy-number profiles suitable for scarHRD (cellularity thresholds pending OCR).
- Pathologic response grading (pCR, near-pCR) is comparable across the retrospective cohort's long accrual window (2004–2016).
- External bibliographic metadata (PubMed/PMC) correctly matches the co-located PDF filename/title.

---

## Limitations / Failure Modes

- **OCR REQUIRED — body not text-extractable:** Co-located PDF could not be parsed with `pdftotext` (not installed), `pypdf`, or `pdfplumber` (Python unavailable on ingestion host). All method details, numeric results, and quotes below are **unverified against the PDF body**.
- **Reference-grade only:** Entry must not drive ideation or feature weights until OCR completes.
- **WES copy-number fragility:** Low purity or low coverage degrades LOH/TAI/LST estimation; paper reportedly filters by cellularity for concordance subset — exact cutoffs pending OCR.
- **Somatic HRR mutations vs HRD scars:** External abstract suggests somatic HRR mutations may not elevate HRD scores like germline mutations — if confirmed, single-gene somatic hits should be deprioritized relative to scar-positive calls (AQ-3).
- **Non-platinum regimen:** HRD–response associations may not generalize to platinum-enriched TNBC neoadjuvant trials that motivate much of the HRD literature.

---

## Key Quantitative or Qualitative Results

**All numeric results pending OCR from co-located PDF.** Do not cite specific effect sizes, correlations, or response rates from this entry.

Expected result categories (to be filled after OCR):

- WES vs OncoScan HRD score correlation and HRD-high/low concordance rate.
- Proportion HRD-high in full cohort and by subtype (TNBC, HER2+, luminal).
- pCR and near-pCR rates in HRD-high vs HRD-low (overall and by subtype).
- HRR mutation frequencies and HRD score differences (germline vs somatic vs wild-type).
- Univariate/multivariate odds ratios for HRD and response (luminal near-pCR analysis referenced in external record).

---

## Key Quotes

**Pending OCR — no direct quotes extracted from co-located PDF.**

After OCR, prioritize quotes defining: (1) WES HRD pipeline commands/parameters, (2) HRD-high threshold justification, (3) WES–array validation statement, (4) primary pCR/near-pCR findings, (5) stated limitations.

---

## Cross-References

### Complements entries in corpus

- **`telli_2016_hrd_score`** (A1): Defines HRD score threshold ≥42 and clinical validation on platinum neoadjuvant TNBC; Kim et al. apply the same scar framework on WES instead of SNP-panel NGS.
- **`davies_2017_hrdetect`** (A1): Alternative HRD detection via multi-signature classifier; contrasts with scar-sum approach used here.
- **`sammut_2022_multiomic_ml`** (A6): Uses scarHRD on WES in TransNEO pCR prediction — Kim et al. provides an independent WES+scarHRD neoadjuvant cohort for method benchmarking.

### Contradicts / Tensions

- **Platinum vs non-platinum neoadjuvant context:** Telli/GeparSixto HRD–platinum associations may not align with P-FEC response patterns emphasized in Kim et al. — interpret HRD predictive value regimen-specifically.
- **Germline vs somatic HRR:** If somatic HRR mutations lack HRD elevation, tension with treating any HRR variant as a high-priority driver (AQ-3).

### Cross-corpus connections

- **A_Genomic_Signal / A1:** HRD scar signal definition and threshold — downstream feature class for candidate genes.
- **E6_Sequencing_Platform (when populated):** WES coverage (reported ~120× tumor / 60× germline in external record), Agilent SureSelect exome capture, pretreatment biopsy handling.
- **D_Clinical_Endpoint:** pCR and near-pCR as endpoints — supporting context for response association (not primary D-corpus placement because main value is method/platform).

### Related entries to add

- **HIGH:** Sztupinszki et al. 2018 — scarHRD NGS migration (`npj Breast Cancer`; cited by Kim et al.).
- **MEDIUM:** Marquard et al. — LOH/TAI/LST component definitions used by scarHRD.
- **LOW:** Riaz et al. HRR gene list curation (referenced for mutation panel).

---

## Author Notes

### Priority justification

**HIGH** (reference) because WES-based HRD computation is a **critical upstream dependency** for the project's genomic signal extraction, and this paper explicitly couples that method to **neoadjuvant breast cancer response** — but ingestion remains reference-grade until OCR.

### Use this source for

- Identifying a **WES + scarHRD** pipeline reference for E1/E6 bridge documentation.
- Framing **AQ-1** data-compatibility questions (can HRD be computed from project WES?).
- Locating **neoadjuvant non-platinum** HRD–response evidence after OCR.
- Cross-checking WES vs SNP-array HRD concordance benchmarks.

### Do NOT use this source for

- Citing specific **pCR effect sizes or ORs** → pending OCR.
- **Direct quotes** or tool version strings → pending OCR.
- **Platinum/PARP stratification** → regimen mismatch; use `telli_2016_hrd_score` or platinum trial literature.
- **HRDetect coefficient weights** → different method; use `davies_2017_hrdetect`.

### Curation notes

- **OCR REQUIRED — body not text-extractable:** PDF extraction failed on ingestion host (`pdftotext` unavailable; Python/`pypdf`/`pdfplumber` unavailable). Re-run OCR or text extraction and upgrade to `corpus_role: decision`.
- **`paper_id` note:** Assigned `kim_2020_hrd_wes` from first author + publication year (DOI 10.1016/j.tranon.2020.100986); not derived from PDF metadata stream.
- **Index updates:** Suggested additions to `CROSS_REFERENCE_INDEX.md` and `README.md` listed in ingestion report (not applied per batch constraints).
- **Harmonize** HRD terminology: NtAI vs TAI; scarHRD vs Myriad HRD assay; near-pCR vs pCR when tagging D-endpoint relevance.

---

## Related Concepts

Kim 2020, WES HRD, whole exome sequencing, scarHRD, Sequenza, PureCN, LOH, TAI, NtAI, LST, genomic scar, HRD-high threshold 42, OncoScan, ASCAT, HRR genes, gHRRm, sHRRm, neoadjuvant chemotherapy, paclitaxel, FEC, P-FEC, pathologic complete response, near-pCR, trastuzumab, breast cancer subtypes, TNBC, luminal, copy number, tumor cellularity, MuTect2, GATK, Agilent SureSelect, platform migration, SNP array replacement

---

## Quality Checklist

- [x] precise terminology of the discipline is used throughout (where not pending OCR)
- [x] the source-type contextualization in Author Notes is complete
- [x] assumptions are explicit
- [x] novel contributions are distinguished from inherited components
- [ ] quantitative or qualitative results include the relevant specifics — **blocked: pending OCR**
- [ ] at least 5 useful direct quotes are included — **blocked: pending OCR**
- [x] cross-references are present (including cross-corpus when relevant)
- [x] the project-relevance relationship section is complete
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated — **deferred per ingestion constraints**
- [ ] the corpus `README.md` registry and counts have been updated — **deferred per ingestion constraints**
