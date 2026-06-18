# Tumor mutational burden and immune infiltration

## Metadata

```yaml
---
paper_id: "tmb_immune_infiltration"
title: "Tumor mutational burden and immune infiltration"
authors: "[UNKNOWN — OCR required; source PDF is image-only merged document without extractable metadata]"
year: null
venue: "[UNKNOWN — OCR required]"
paper_type: "[UNKNOWN — likely primary_research or review; confirm after OCR]"
domain: "A_Genomic_Signal"
subdomain: "TMB and immune infiltration"
relevance_score: 3
priority_level: "MEDIUM"
corpus_role: "reference"
temporal_status: "active_candidate"
relevance_tags:
  - "TMB"
  - "tumor_mutational_burden"
  - "neoantigen_load"
  - "immune_infiltration"
  - "TILs"
  - "CD8_T_cells"
  - "checkpoint_immunotherapy"
  - "WES"
  - "response_biomarker"
  - "prognostic_biomarker"
  - "A2_TMB"
  - "A3_immune_microenvironment"
  - "OCR_REQUIRED"
doi: ""
isbn: ""
url: ""
pdf_file: "tmb_immune_infiltration.pdf"
ingestion_note: "paper_id is a placeholder slug — firstauthor_year could not be determined because the co-located PDF is a non-extractable image stream (PDFsam Basic v6.0.1 merge, 2026-06-17). Rename after OCR identifies the constituent article(s)."
---
```

---

## One-Sentence Summary

**Placeholder reference entry** for a merged, image-only PDF titled *Tumor mutational burden and immune infiltration* — the topic bridges A2 (TMB as a WES-derivable mutational-load signal) and A3 (immune infiltration / TIL biology) and is directly relevant to AQ-1 and AQ-3, but **no body text could be extracted**; OCR and re-ingestion are required before this source can support decision-level claims about pCR or neoadjuvant response.

---

## Key Contributions

> **⚠ OCR REQUIRED — contributions below are inferred from the document title and filename only, not from verified body text. Do not cite as evidence until re-ingested.**

- Likely addresses the **relationship between tumor mutational burden (TMB) and immune cell infiltration** in the tumor microenvironment — a mechanistic link central to both A2 and A3 genomic signal classes.
- May discuss TMB and/or immune infiltration as **response or prognostic biomarkers** (filename and staging-folder context; unverified).
- Co-located PDF is a **PDFsam Basic merge** (`Tumor mutational burden and immune infiltration_merged.pdf`) — may contain **one or more constituent articles** that must be separated and identified after OCR.

---

## Core Idea / Mechanism / Argument

### What this source likely claims (title-inferred only)

Based solely on the filename and corpus placement intent, the source probably engages the **TMB → neoantigen → adaptive immunity** axis: somatic mutation load increases candidate neoantigens; processed peptides presented on MHC can recruit and expand tumor-infiltrating lymphocytes (TILs), especially CD8⁺ T cells. Papers on this topic often further ask whether **TMB**, **immune infiltration scores**, or their **combination** predicts treatment response (notably checkpoint blockade) or prognosis.

**None of the above is verified against this PDF's body.** Treat as a retrieval placeholder until OCR completes.

### Established domain context (general field knowledge — not attributed to this PDF)

The following is **background biology** useful for agents retrieving this entry; it is **not** extracted from or endorsed by the co-located source:

1. **TMB definition:** Non-synonymous somatic mutation count normalized per megabase of sequenced territory (convention varies: coding exome vs whole genome; panel size affects comparability).
2. **Mechanistic link:** Higher mutational load → increased neoantigen repertoire → potential for enhanced antitumor T-cell recognition, subject to antigen presentation, clonal deletion, and immune-editing constraints.
3. **Immune infiltration readouts:** Histologic TIL density, gene-expression signatures (e.g., IFN-γ/T-cell inflamed signatures), or deconvolution of bulk RNA — only partially overlapping with DNA-derived TMB.
4. **Concordance is imperfect:** TMB-high tumors can be immune-desert; TMB-low tumors can show brisk TIL infiltration (e.g., viral, mismatch-repair, or non-mutation-driven immune activation).
5. **Breast cancer context (project boundary):** Basal/TNBC tends toward higher TMB and TIL density than luminal disease; HER2+ occupies an intermediate immune landscape. Neoadjuvant **pCR** in TNBC/HER2+ is often associated with immune activation, but effect sizes and gene-level drivers require **primary breast neoadjuvant studies**, not generic TMB–immune reviews.
6. **Therapeutic bridge:** TMB and immune infiltration jointly inform **checkpoint immunotherapy** stratification (`B_Therapeutic_Context` / B3) — distinct from chemotherapy-only neoadjuvant regimens unless trial arms include immunotherapy.

### Claimed vs demonstrated

| Status | Content |
|--------|---------|
| **Claimed (this entry)** | Nothing — body unreadable. |
| **Demonstrated (this entry)** | Nothing — body unreadable. |
| **Inferred (title only)** | Source topic = TMB × immune infiltration as biomarker/mechanism axis. |

---

## Methodology / Evidence Base

> **⚠ OCR REQUIRED — entire section pending document access.**

### Known file properties (verified)

| Property | Value |
|----------|-------|
| Original filename | `Tumor mutational burden and immune infiltration_merged.pdf` |
| Merge tool | PDFsam Basic v6.0.1 (XMP metadata) |
| Merge date | 2026-06-17 |
| PDF version | 1.5 |
| Text extractability | **Failed** — image/stream-encoded pages; no selectable text layer |
| Extraction attempts | `pdftotext` (not installed); `pypdf` / `pdfplumber` (Python unavailable on ingestion host); raw-byte ASCII scan found no title/abstract strings |

### Pending after OCR

- Study design (cohort, trial, review, meta-analysis)
- Cancer type(s) and whether **breast / TNBC / HER2+** subsets are included
- TMB measurement platform (WES, WGS, targeted panel) and cutoff definitions
- Immune infiltration assay (IHC TILs, RNA signature, spatial, flow)
- Endpoint type (**pCR** vs OS/PFS vs ORR to immunotherapy)
- Sample sizes and effect sizes

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus:** `A_Genomic_Signal` — primary placement `A2_Tumor_Mutational_Burden`; strong secondary link to `A3_Immune_Microenvironment`
- **Anchor question(s):** **AQ-1** (WES mutational features correlated with pCR); **AQ-3** (prioritize high-signal genomic/immune features vs background noise)
- **Bridge corpora:** `B_Therapeutic_Context` (**B3** checkpoint immunotherapy — TMB/immune co-stratification); `A3_Immune_Microenvironment` (TIL / T-cell infiltration readouts); `D_Clinical_Endpoint` (once endpoint and effect sizes are verified); `E_Study_Type` (WES/panel method defining TMB)

### How it could be used

- **Directly reusable:** **Not yet** — requires OCR and breast/neoadjuvant/pCR relevance check.
- **Indirectly inspiring:** **Yes, as a topic pointer** — flags the TMB–immune co-axis as a joint A2/A3 feature class worth extracting from WES + transcriptomic or pathology layers.
- **Mainly background / framing:** **Current status** — domain context above supports agent reasoning about why TMB and immune infiltration should be co-indexed, but this specific PDF adds no verified evidence until re-ingested.

### Main fit with the project

If the underlying article(s) include **breast cancer neoadjuvant cohorts** with WES-derived TMB and immune infiltration measures tied to **pCR**, this source could become a decision-level bridge between mutational load (A2) and microenvironmental response (A3) — exactly the multi-signal pattern the project prioritizes for TNBC/HER2+.

### Main mismatch or risk

- **Non-extractable PDF** — highest immediate risk; all metadata except filename is unknown.
- **Merged document** — may bundle heterogeneous studies; agents must not treat as a single citation.
- **Topic generality** — TMB–immune literature is often pan-cancer and immunotherapy-focused; project scope is **breast-only** and **pCR-primary**; many sources fail the boundary test.
- **Endpoint drift** — immune/TMB papers frequently report survival or ICI response, not neoadjuvant pCR.

### Concrete follow-up

1. **Run OCR** on `tmb_immune_infiltration.pdf`; identify constituent article(s), DOI, authors, year → rename to `firstauthor_year_keyword`.
2. Re-ingest as **`corpus_role: decision`** only if body confirms breast neoadjuvant pCR (or clearly treatment-predictive WES features for project's regimens).
3. Cross-link verified immune genes/signatures to **`A3_Immune_Microenvironment`** entries once text is available.
4. If immunotherapy arms appear, add **`B3`** bridge tags in `B_Therapeutic_Context` index.

---

## Assumptions

- The filename reflects the **intellectual content** of the merged PDF (reasonable but unverified).
- The merge contains **scientific article PDF(s)**, not slides or unrelated documents (unverified).
- **General domain biology** summarized above reflects current mainstream understanding; it is included only as retrieval context, not as claims by this source.
- Until OCR, **no quantitative or author-specific statements** from this PDF should propagate to AQ-1/AQ-3 rankings.

---

## Limitations / Failure Modes

- **⚠ OCR REQUIRED:** The co-located PDF is an image-encoded stream without a text layer. All standard extraction tools failed on the ingestion host (`pdftotext` unavailable; Python/`pypdf`/`pdfplumber` unavailable). **This entry must not be upgraded to `decision` role or cited for effect sizes until OCR re-ingestion.**
- **Unknown authorship and provenance** — cannot assess peer-review status, cohort quality, or conflicts.
- **Merged PDF structure** — page boundaries between constituent documents unknown; citation risk if treated as monolithic.
- **Placeholder `paper_id`** — registry collisions possible if multiple OCR-unknown TMB sources exist; rename promptly after identification.
- **Breast / pCR applicability unknown** — title-level TMB–immune sources often address pan-cancer ICI, which may be **out of scope** for the project's primary endpoint even after OCR.

---

## Key Quantitative or Qualitative Results

> **None extracted.** Do not infer numbers from this entry. Re-ingest after OCR.

---

## Key Quotes

> **⚠ OCR REQUIRED — no direct quotes.** Extraction produced zero usable body text. Quotes must be added only from OCR-verified text in a future re-ingestion pass. **Do not fabricate.**

---

## Cross-References

### Complements entries in corpus

- **`sammut_2022_multiomic_ml`** (A6): Multi-omic ML integrates genomic and immune microenvironment features for therapy response — parallel integrated-signal framing once this source is readable.
- **`davies_2017_hrdetect` / `telli_2016_hrd_score`** (A1): Independent DNA-repair deficiency signal; TMB and HRD can co-occur but measure different biology — compare after OCR to avoid double-counting repair-deficiency drivers.

### Contradicts / Tensions

- **TMB vs TIL concordance (field tension):** Literature reports both correlation and discordance between mutational load and infiltration; this source may adjudicate context — **unreadable until OCR**.
- **A2 vs A3 feature independence:** If the paper argues TMB subsumes immune signal (or vice versa), AQ-3 prioritization must treat one axis as derivative — **pending OCR**.

### Cross-corpus connections

- **`B_Therapeutic_Context` / B3:** TMB-high and T-cell-inflamed phenotypes stratify checkpoint immunotherapy; bridge only if the underlying study's treatment arms match project regimens.
- **`A3_Immune_Microenvironment`:** Shared biology — infiltration scores, TIL density, IFN-γ signatures; ingest companion A3 entry or cross-tag after OCR.
- **`D_Clinical_Endpoint`:** Verify whether endpoints are pCR (in scope) vs survival/ICI ORR (supporting context only).
- **`E_Study_Type`:** TMB computation depends on sequencing depth, panel size, and caller — method metadata must be captured on re-ingestion.

### Related entries to add

- **HIGH:** OCR-identified primary article(s) from this merge, renamed to canonical `paper_id`.
- **HIGH:** Breast neoadjuvant WES studies linking **TMB**, **TILs**, and **pCR** in TNBC/HER2+ (if not already in merge).
- **MEDIUM:** FDA/KEYNOTE-158 TMB-high pan-tumor immunotherapy label context (reference only; non-breast-primary).
- **LOW:** Pan-cancer TMB–immune correlation meta-analyses unless breast subset data are reported.

---

## Author Notes

### Priority justification

**MEDIUM** priority and **relevance_score 3** — the *topic* is central to A2/A3 and AQ-1/AQ-3, but the *ingested artifact* is presently unusable for evidence-based reasoning. Priority rises after OCR if breast neoadjuvant pCR data are confirmed.

### Use this source for

- Locating the **TMB × immune infiltration** thread in the A2 folder pending full text
- Understanding **why A2 and A3 should be cross-indexed** (domain framing section only)
- Triggering **OCR workflow** for merged Doc_brute staging files
- Planning **WES feature extraction** that pairs mutational load with immune readouts

### Do NOT use this source for

- **Effect sizes, p-values, thresholds, or quotes** → OCR required
- **AQ-3 driver ranking** → no gene-level evidence ingested
- **pCR prediction claims** → endpoint unverified
- **Clinical immunotherapy decisions** → out of project scope for treatment advice

### Curation notes

- **⚠ OCR REQUIRED — prominent.** Re-ingest with full template (quotes, methods, results) after text extraction.
- **`paper_id` placeholder:** `tmb_immune_infiltration` used because `firstauthor_year` could not be determined; update registry on rename.
- **Merged PDF:** Inspect page breaks post-OCR; split into separate corpus entries if multiple articles.
- **Harmonize TMB units** (mut/Mb coding vs WGS) when re-ingesting.
- **Update `CROSS_REFERENCE_INDEX.md`** Concepts rows for **TMB** and **Immune infiltration** after OCR confirms content.
- **Update `README.md` registry** (A2 count + one-line description) after OCR — deferred per ingestion constraints.

---

## Related Concepts

tumor mutational burden, TMB, mutational load, neoantigen, neoantigen load, immune infiltration, tumor-infiltrating lymphocytes, TILs, CD8+ T cells, T-cell inflamed signature, IFN-γ signature, antigen presentation, MHC, immune desert, immune excluded, checkpoint immunotherapy, PD-1, PD-L1, WES, whole exome sequencing, response biomarker, prognostic biomarker, pCR, neoadjuvant, TNBC, HER2-positive breast cancer, A2, A3

---

## Quality Checklist

- [x] precise terminology of the discipline is used throughout
- [x] the source-type contextualization in Author Notes is complete
- [x] assumptions are explicit
- [x] novel contributions are distinguished from inherited components (none verified from source)
- [x] quantitative or qualitative results include the relevant specifics (none — explicitly flagged)
- [ ] at least 5 useful direct quotes are included *(blocked — OCR required)*
- [x] cross-references are present (including cross-corpus when relevant)
- [x] the project-relevance relationship section is complete
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated *(deferred per ingestion constraints)*
- [ ] the corpus `README.md` registry and counts have been updated *(deferred per ingestion constraints)*
