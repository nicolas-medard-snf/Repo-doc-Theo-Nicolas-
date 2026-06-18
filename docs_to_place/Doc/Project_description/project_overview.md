# Project Overview


## 1. What this project is

The goal of this project is to predict the pathological complete response (pCR) of TNBC and HER2+ breast cancers to neoadjuvant treatments. The analysis relies on genomic profiling, specifically leveraging Whole Exome Sequencing (WES) data

## 2. Goals and anchor questions

The project is organized around a small set of **anchor questions** — the questions the knowledge system exists to help answer.

- **AQ-1**: What specific mutational driver identified via Whole Exome Sequencing (WES) are significantly correlated with achieving a pathological complete response (pCR) in TNBC or HER2+ breast cancer patients?
- **AQ-2**: How do the identified genomic biomarkers differentiate between a patient's response to neoadjuvant chemotherapy versus targeted therapies (such as anti-HER2 agents or immunotherapies) within these specific breast cancer subtypes?
- **AQ-3**: Based on the provided literature, which genes can be confidently classified as 'high-priority drivers' of neoadjuvant treatment response, and which can be deprioritized as genomic background noise to optimize downstream dataset analysis?

Every corpus entry's `Relationship with the project's goals` section should connect back to at least one anchor question.

## 3. Corpora

List the corpora this project curates. Each becomes a directory under `Doc/Corpus/` and gets one expert agent (`.cursor/Agents/expert_<short_name>.md`).

| Short name | Corpus directory | Scope (one line) |
|------------|------------------|------------------|
| Genomic_Signal | `Doc/Corpus/A_Genomic_Signal/` |  defines the biological feature class (HRD, TMB, immune, drivers/CNV, epigenetics) each candidate gene belongs to |
| Therapeutic_Context | `Doc/Corpus/B_Therapeutic_Context/` | A gene only predicts response for a specific drug, so this matches biomarkers to the relevant treatment |
| Cancer_Subtype | `Doc/Corpus/C_Cancer_Subtype/` | Predictive value is subtype-dependent, preventing a TNBC biomarker from being misapplied to HR+/HER2+ data |
| Clinical_Endpoint | `Doc/Corpus/D_Clinical_Endpoint/` | Relevance filter that prioritizes genes tied directly to pCR over softer outcomes (survival, resistance) |
| Study_Type | `Doc/Corpus/E_Study_Type/` | Tells the AI what kind of evidence and sequencing data each paper provides (method, model, trial, cohort, platform) |

## 4. How the corpora relate (bridges)

Describe the most important relationships between corpora — which corpus supplies upstream ideas for which other corpus. These bridges drive the `cross-corpus-enrichment-analysis` skill.

- E_Study_Type → A_Genomic_Signal : Most upstream. Methods/algorithms (HRDetect, HRD-score, WES/NGS migration) define how each genomic signal is computed — without E's tooling, A's features can't be extracted from raw sequence.
- A_Genomic_Signal → B_Therapeutic_Context : A supplies the candidate biomarkers/genes; B is where they gain meaning, since each signal maps to a drug it predicts (HRD→PARP/platinum, immune→checkpoint, ERBB2→anti-HER2).
- C_Cancer_Subtype → B_Therapeutic_Context : Subtype dictates the treatment regimen and gates which A-signal is even relevant, so C conditions both A's interpretation and B's drug selection.
- A_Genomic_Signal + B_Therapeutic_Context + C_Cancer_Subtype → D_Clinical_Endpoint : D is the downstream sink — the genomic signal, in its treatment and subtype context, is validated against pCR. Multi-omic/ML and trial papers live at this convergence.
- D_Clinical_Endpoint → A_Genomic_Signal : Validated pCR outcomes feed back to re-rank which genomic signals in A deserve priority, tightening the candidate-gene shortlist over time.



## 5. Boundaries

State explicitly what is **out of scope** so agents do not drift:

- Non-breast cancers — no lung, ovarian, colorectal, etc., even if they share biomarkers (HRD, TMB). Breast only.
- Non-pCR endpoints as primary targets — survival, recurrence, toxicity, and resistance are supporting context only (Axis D2/D3), never the prediction goal, which is pCR.
- Non-predictive biology — pure tumorigenesis/etiology, epidemiology, risk/screening, prognosis-without-treatment, and germline risk genetics (unless they define a treatment-predictive signal).
- Therapies outside the corpus's treatment axis — endocrine-only, radiotherapy, surgery technique, supportive care, and any drug class not tied to a B1–B4 context.
- Non-DNA-derivable signals as standalone targets — proteomics, metabolomics, pure imaging/radiomics, and clinical-only variables are not the gene-level focus; digital pathology and transcriptomics enter only as part of an integrated multi-omic signal.
- Variant interpretation beyond predictive relevance — no exhaustive VUS curation, pharmacogenomics of drug metabolism, or population-genetics analysis.
- Source file integrity — no moving, renaming, or deleting files in Doc_brute; ingestion is copy/tag only.
- Fabricated content — no invented abstracts, genes, or metrics; image-only or non-extractable PDFs are flagged for OCR instead.
- Taxonomy changes — no new axes or categories beyond A–E without explicit approval, and no silently merging or adding a sixth axis.
- Clinical recommendations — the corpus informs gene prioritization for a downstream AI, not patient treatment decisions.

## 6. Priority

If one corpus should be grown first, say which and why:

- **Priority corpus**: Genomic_Signal — It is the only axis whose content is gene/feature-level (BRCA1/2, HRD signatures, TMB, immune genes, drivers, chromatin regulators) and therefore the one that actually produces the candidate genes the project exists to surface. The other axes (B, C, D, E) are merely context filters that stay useless until there is a gene list to filter. Per the pipeline flow E → A → (C) → B → D, A is the first axis that generates the substrate everything downstream consumes, so a thin A starves B/C/D of anything to contextualize; it is also the highest-leverage and cheapest-to-validate axis, since your strongest current assets (HRDetect, HRD-score, the WGS landscape, TMB/immune, multi-omic) are already A-heavy and gene-level claims are concrete and checkable against datasets. Practically, prioritize A1 (HRD/DNA-repair) and A3 (immune microenvironment) first, as they hold the most established, treatment-linked pCR biomarkers in breast cancer and thus give the downstream AI usable candidates earliest, while adding B/C tags opportunistically during ingestion rather than blocking on them.
