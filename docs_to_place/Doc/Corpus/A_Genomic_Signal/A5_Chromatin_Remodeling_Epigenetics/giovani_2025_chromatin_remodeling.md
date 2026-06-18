# Chromatin remodeling complexes: architects influencing breast cancer progression

## Metadata

```yaml
---
paper_id: "giovani_2025_chromatin_remodeling"
title: "Chromatin remodeling complexes: architects influencing breast cancer progression"
authors: "Octavianus Giovani, Grace S. Eckersley, Hayden R. Jones, Sankari Nagarajan"
year: 2025
venue: "Frontiers in Cell and Developmental Biology"
paper_type: "review"
domain: "A_Genomic_Signal"
subdomain: "chromatin remodeling / epigenetic regulators"
relevance_score: 3
priority_level: "MEDIUM"
corpus_role: "reference"
temporal_status: "active_candidate"
relevance_tags:
  - "SWI/SNF"
  - "BAF"
  - "PBAF"
  - "ncBAF"
  - "ISWI"
  - "CHD"
  - "NuRD"
  - "INO80"
  - "ARID1A"
  - "SMARCA4"
  - "SMARCA2"
  - "PBRM1"
  - "CHD4"
  - "BPTF"
  - "epigenetic_regulators"
  - "synthetic_lethality"
  - "TNBC"
  - "HER2"
  - "endocrine_resistance"
  - "gene_catalog"
doi: "10.3389/fcell.2025.1690350"
isbn: ""
url: "https://doi.org/10.3389/fcell.2025.1690350"
pdf_file: "giovani_2025_chromatin_remodeling.pdf"
---
```

---

## One-Sentence Summary

Giovani et al. (2025) synthesize breast-cancer evidence across four ATP-dependent chromatin-remodeling subfamilies (SWI/SNF, ISWI, CHD, INO80), cataloging named subunits with proposed tumor-suppressive vs oncogenic roles in progression, aggressiveness, and therapy resistance — a gene-level background map for the A5 epigenetic-regulator class that supports AQ-3 candidate prioritization but does not report neoadjuvant pCR associations.

---

## Key Contributions

- Organizes human ATP-dependent remodelers into **four subfamilies** (SWI/SNF, ISWI, CHD, INO80) and three SWI/SNF assemblies (BAF, PBAF, ncBAF), with structural domain distinctions (DExx/HELICc ATPase, bromodomain, HSA, HSS, tandem chromodomains).
- Provides **Table 1**, a breast-cancer-specific catalog of subunit-level functional and correlative evidence with proposed tumor-suppressive vs oncogenic classifications.
- Reviews **subtype-linked biology** (luminal A/B, HER2-enriched, TNBC) and links remodeler alterations to proliferation, EMT, metastasis, DNA repair, immune escape, and endocrine/chemotherapy resistance.
- Surveys **direct and indirect therapeutic strategies** (ATPase inhibitors, PROTAC degraders, synthetic lethality with PARP/ATR, HDAC/BET/EZH2 combinations) largely extrapolated from non-breast or preclinical models.
- Highlights **context-dependent dual roles** (e.g., BRG1/BRM as tumor suppressor or promoter; CHD4 as suppressor in some contexts but oncogenic in breast) and the need for molecular profiling before targeting.

---

## Core Idea / Mechanism / Argument

### Claimed vs demonstrated

**Claimed:** Chromatin remodeling complexes are essential drivers of breast cancer progression and aggressiveness; their subunits are attractive therapeutic targets via direct ATPase/bromodomain inhibition or indirect synthetic-lethality and epigenetic combinations; further profiling will delineate tumor-suppressor vs coactivator activity in a subtype-specific manner.

**Demonstrated (as review synthesis):** The authors compile published functional studies (knockout/knockdown, ChIP-seq, IHC, cohort analyses from TCGA/METABRIC/cBioPortal) into a structured gene-by-gene summary. They do **not** present new primary cohort data or pCR outcome analyses.

### Information flow

1. **Breast cancer heterogeneity** — molecular subtypes (ER/PR/HER2; luminal A/B, HER2-enriched, TNBC) set the clinical context for remodeler relevance.
2. **Remodeler taxonomy** — four ATP-dependent families with distinct ATPase subunits and accessory modules regulate nucleosome sliding, ejection, assembly, and histone editing.
3. **Subunit → phenotype mapping** — for each named subunit, literature is summarized for proliferation, migration/invasion, DNA repair, hormone signaling, immune modulation, and therapy response.
4. **Alteration landscape** — TCGA/METABRIC alteration frequencies (Figure 4) anchor which genes are recurrently mutated, deleted, or amplified.
5. **Therapeutic translation** — inhibitors/degraders and synthetic-lethal pairs are discussed as future directions, with explicit caveats on subtype heterogeneity and dual tumor-suppressor/oncogene roles.

### Novel vs inherited

- **Inherited:** Decades of chromatin-remodeling biochemistry (Clapier & Cairns; Kadoch & Crabtree); prior cancer-genomics catalogs of SWI/SNF mutations (~20% of cancers); primary studies cited per subunit (Nagarajan et al. on ARID1A/endocrine resistance; Thang et al. on INO80 in basal breast cancer; CHD4/HER2 signaling work by D'Alesio et al., etc.).
- **Novel (this review):** Integrated 2025 breast-focused synthesis across all four families in one Table 1 + therapeutic landscape figure; explicit framing of IDR regions in ARID1A/ARID1B as undruggable but therapeutically relevant; updated discussion of PROTAC agents (AU-15330, FHD-286, BRD9 degraders) and breast cell-line resistance to AU15330.

### Named complexes, genes, and proposed roles in breast cancer

#### SWI/SNF (BAF / PBAF / ncBAF)

| Subunit (gene) | Proposed role in breast cancer (per review) | Notes from review |
|----------------|---------------------------------------------|-------------------|
| BRG1 / **SMARCA4** | **Oncogenic** (primary); also tumor suppressor in some contexts | High expression in primary breast cancer; coactivates ER signaling; promotes fatty acid synthesis in TNBC; interacts with BRCA1/TP53 as suppressor pathway |
| BRM / **SMARCA2** | Context-dependent; loss can promote proliferation | Inverse correlation with malignancy via Claudin epigenetic activation in some studies; essential for proliferation in knockdown models |
| **ARID1A** | **Tumor suppressive** | 78% of TNBCs show low expression; loss linked to endocrine resistance, PIK3CA/PTEN/p53 co-alterations, DNA repair (end resection) |
| **ARID1B** | **Oncogenic** | Highly expressed in TNBC; synthetic-lethality partner of ARID1A; prognostic marker |
| **PBRM1** | **Tumor suppressive** | Binds p21 promoter; low expression → poor prognosis; also implicated in immune resistance in preclinical models |
| **ARID2** | **Tumor suppressive** | Reduced in non-luminal subtypes; poor survival predictor in ER+ disease; recurrent inactivation in metastatic disease |
| **SMARCB1**, **SMARCE1**, **SMARCC1/2**, **SS18**, **SS18L1** | Core/accessory; complex integrity | SMARCD2, BCL7C, SS18L1 amplified in 6–8% (TCGA/METABRIC) |
| **SMARCD2**, **SMARCD3**, **BCL7C** | Mixed / under-studied | SMARCD3 IHC linked to cell-cycle regulators (Tropée et al.) |
| **DPF1/2/3**, **PHF10**, **BRD7**, **BRD9**, **BICRA**, **BICRAL** | Accessory defining BAF/PBAF/ncBAF | BRD9 in synthetic lethality with SMARCB1; ncBAF dependency noted in other cancers |

#### ISWI

| Subunit (gene) | Proposed role | Notes |
|----------------|---------------|-------|
| **SMARCA5** | **Oncogenic** | Overexpression correlates with stage and poor survival; G1→S transition, MMP2-mediated invasion |
| **SMARCA1** | **Oncogenic** (with conflicting prognostic data) | Supports survival; downregulation reported in some cohorts |
| **BAZ1A** | **Oncogenic** (correlative) | Senescence regulator; poor OS/RFS; amplification → short metastasis-free survival |
| **BAZ1B** | **Oncogenic** | Amplified; drives CYP19A1/ESR1 → aromatase inhibitor resistance |
| **BPTF** | **Oncogenic** | Frequent amplification; advanced grade in ER+ and TNBC; immune escape via NURF complex |
| **CECR2** | **Oncogenic** | Metastasis; M2 macrophage polarization via NF-κB/CSF1/CXCL1 |
| **CHRAC1**, **POLE3** | Upregulated | CHRAC1 driver on 8q24.3; interacts with YAP |
| **RSF1** | **Oncogenic** (p53-dependent) | Overexpression with p53 mutation selects for proliferation |
| **RBBP4**, **RBBP7** | Context-dependent | NURF/HDAC complexes; RBBP4–BCL11A chemoresistance in TNBC stem cells |
| **BAZ2B** | Downregulated in primary disease | Role unclear |

#### CHD (often within NuRD)

| Subunit (gene) | Proposed role | Notes |
|----------------|---------------|-------|
| **CHD1** | **Oncogenic** (proliferation); also inactivating mutations reported | Estrogen–microRNA axis; c-MYC interaction |
| **CHD2** | Likely tumor suppressive | Less studied in breast |
| **CHD3** | **Tumor suppressive** (correlative) | ~60% heterozygous loss |
| **CHD4** | **Oncogenic** in breast (review emphasis) | NuRD component; amplifications common; drives HER2/PI3K/AKT/ERK, EMT, β1-integrin; depletion reduces tumor mass in HER2+ and TNBC models |
| **CHD5** | **Tumor suppressive** | Loss via methylation/deletion; activates CDKN2A; represses WEE1 |
| **CHD7** | **Oncogenic** | ~11% amplification; aggressive subtypes; NRAS targets |
| **CHD8** | Dual | Top tumor suppressor by mutation frequency; also estrogen/cyclin D1 proliferation axis |
| **CHD9** | **Tumor suppressive** (correlative) | ~55% heterozygous loss |

#### INO80

| Subunit (gene) | Proposed role | Notes |
|----------------|---------------|-------|
| **INO80** | **Tumor suppressive** (expression) | Downregulated in basal-type; low expression → worse OS/DMFS/RFS; regulates H2A.Z at ER target enhancers (GREB1, TFF1) |
| **SRCAP** | **Oncogenic** | miRNA-641 axis (LINC00665); proliferation/invasion |
| **UCHL5** (UCH37) | **Oncogenic** | Amplified; deubiquitinates E2F1; TGF-β pathway |
| **VPS72** (YL1) | Amplified | Shared SRCAP/TIP60/p400 subunit; prognostic candidate |
| **TRRAP**, **EP400** (p400), **TIP60**, **BRD8**, **EPC1**, **ING3**, **ACTR6**, **DMAP1**, **GAS41**, **MBTD1** | p400/TIP60 module | Regulate H2A.Z/H3.3 exchange; E2F1/p53/MYC transcriptional control |

---

## Methodology / Evidence Base

### If conceptual / theoretical / synthesis

- **Theoretical framework invoked:** ATP-dependent chromatin remodeling as a gatekeeper of transcription, DNA repair, and nucleosome editing; SWI/SNF as broadly tumor-suppressive complex with oncogenic ATPase exceptions; synthetic lethality and epigenetic vulnerability as therapeutic logic.
- **Sources drawn upon:** Primary functional studies (cell-line knockdown/knockout, PDX/transgenic mouse models, ChIP-seq), clinicopathological cohort analyses (METABRIC, TCGA via cBioPortal), and preclinical drug-development literature (mostly non-breast cancers for PROTAC/ATPase inhibitors).
- **Position in the existing debate:** Accepts context-specific dual roles rather than single gene = single function; emphasizes that blanket SWI/SNF inhibition may harm tumor-suppressor functions (ARID1A, BRG1 in ER+ disease).

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus:** `A_Genomic_Signal` — category `A5_Chromatin_Remodeling_Epigenetics`
- **Anchor question(s):** **AQ-3** (high-priority drivers vs genomic background noise in the epigenetic-regulator class); secondary framing for **AQ-1** only insofar as named WES-detectable alterations (mutations, deletions, amplifications) are cataloged — no pCR effect sizes provided
- **Bridge corpus (if relevant):** `B_Therapeutic_Context` (chemotherapy/endocrine/immune checkpoint sensitization); `C_Cancer_Subtype` (TNBC, HER2+, luminal/endocrine resistance); `D_Clinical_Endpoint` (prognosis/survival/resistance — not pCR)

### How it could be used

- **Directly reusable:** Gene-level checklist of chromatin-remodeling subunits with proposed directional roles (oncogenic vs tumor-suppressive) for initial WES feature tagging in the A5 class.
- **Indirectly inspiring:** Synthetic-lethality pairs (ARID1A↔ARID1B, ARID1A→PARP/ATR, BRG1-deficient→SMARCA2 degradation) as hypotheses for why certain remodeler mutations might co-occur with DNA-repair or HRD signals already tracked in A1.
- **Mainly background / framing:** Mechanistic vocabulary (BAF/PBAF/ncBAF, NuRD, H2A.Z editing) and therapy-resistance biology without neoadjuvant outcome data.

Explain why, specifically: The review exhaustively names remodeler genes altered in breast cancer and classifies them for aggressiveness/progression — exactly the substrate AQ-3 needs to separate plausible A5 candidates from undifferentiated "chromatin gene" noise — but it never tests or reports pathological complete response to neoadjuvant therapy.

### Main fit with the project

- Supplies a **curated gene catalog** spanning SWI/SNF, ISWI, CHD, and INO80 subunits with breast-specific functional annotations, enabling WES pipelines to tag mutations/CNVs in ARID1A, SMARCA4, PBRM1, CHD4, BPTF, INO80, etc., as members of a coherent biological feature class.
- Links several A5 genes to **DNA repair** (ARID1A end resection; CHD3/CHD4–PARP; SWI/SNF–BRCA1–TP53), creating natural cross-tags to `A1_HRD_Mutational_Signatures_DNA_Repair`.
- Documents **subtype specificity** (TNBC enrichment for ARID1A loss, ARID1B high expression; basal-type INO80 downregulation; HER2+ CHD4 signaling), supporting downstream `C_Cancer_Subtype` filtering.

### Main mismatch or risk

- **Not a pCR-prediction study.** Endpoints are progression, aggressiveness, survival, metastasis, and therapy resistance — not neoadjuvant pathological complete response. Genes prioritized here for "oncogenic" proliferation roles may not predict chemotherapy clearance at surgery.
- **Review-level evidence** — classifications in Table 1 inherit mixed study quality; many entries rely on expression or alteration frequency rather than causal WES–outcome associations.
- **Context-dependent dual roles** — BRG1/BRM, CHD4, CHD8, and complex-level tumor-suppressor labels conflict with subunit-level oncogenic data; naive AQ-3 ranking from this source alone would over-prioritize or mis-rank genes without subtype and alteration-type context.
- **Therapeutic sections extrapolate** from lung, ovarian, and other cancer models (AU-15330, FHD-286); breast cell lines MCF7, MDA-MB-486, MDA-MB-231 reported resistant to AU15330.

### Concrete follow-up

- Cross-check Table 1 high-frequency altered genes (ARID1A, SMARCA4, CHD4, BPTF, CHD7, UCHL5) against any future **D_Clinical_Endpoint** neoadjuvant WES cohorts for actual pCR associations before promoting to high-priority drivers.
- Flag **ARID1A**, **SMARCA4**, **PBRM1**, **CHD4**, **BPTF**, **INO80** for index entries under "Chromatin remodeling / epigenetic regulators" and AQ-3.
- Seek decision-grade primary studies linking remodeler mutations to **neoadjuvant pCR** in TNBC/HER2+ (gap exposed by this review).

---

## Assumptions

- TCGA and METABRIC alteration frequencies reasonably represent invasive breast cancer genomics.
- Functional classifications from cell-line and mouse models extrapolate to human tumor biology and WES-detectable events.
- Tumor-suppressive vs oncogenic labels in Table 1 reflect the authors' synthesis of cited literature as of 2025, not a unified statistical meta-analysis.
- Therapy sections assume synthetic-lethality relationships validated in non-breast systems may transfer to breast subtypes with matching alterations.

---

## Limitations / Failure Modes

- **No primary data or systematic meta-analysis** — risk of citation bias toward well-studied SWI/SNF genes (ARID1A, SMARCA4) over under-documented INO80/SRCAP biology.
- **Dual-role genes** — BRG1/BRM and CHD4 can appear oncogenic or suppressive depending on subtype and assay; a single AQ-3 priority label from this review will be wrong without additional context.
- **Expression vs mutation conflation** — low ARID1A mRNA/IHC does not equal WES LOF; amplification of BPTF/CHD7 differs mechanistically from truncating SWI/SNF mutations.
- **Endpoint mismatch for the project** — survival, relapse, and endocrine resistance findings do not validate pCR predictive value.
- **Therapeutic generalization** — PROTAC/ATPase inhibitor efficacy and toxicity data largely from non-breast trials; AU15330 resistance in breast lines warns against treating drugability as biomarker priority.

---

## Key Quantitative or Qualitative Results

### Table 1 functional classifications (breast cancer, per review)

| Complex | Subunit | Proposed classification |
|---------|---------|-------------------------|
| SWI/SNF | BRG1/BRM (SMARCA4/2) | Oncogenic |
| SWI/SNF | ARID1A | Tumor suppressive |
| SWI/SNF | ARID1B | Oncogenic |
| SWI/SNF | PBRM1 | Tumor suppressive |
| SWI/SNF | ARID2 | Tumor suppressive |
| ISWI | SMARCA5, SMARCA1, BAZ1A, BPTF, CECR2 | Oncogenic |
| CHD | CHD1, CHD4, CHD7 | Oncogenic |
| CHD | CHD3, CHD5, CHD9 | Tumor suppressive |
| INO80 | INO80 | Tumor suppressive (expression) |
| INO80 | SRCAP | Oncogenic |

### Selected quantitative findings cited in the review

- ~**20%** of all cancers harbor mutations in SWI/SNF subunit genes (Kadoch et al., 2013).
- **78%** of TNBCs exhibit low ARID1A expression (Zhang et al., 2012).
- **~58%** of ARID1A/ARID1B mutations occur in intrinsically disordered regions (Patil et al., 2023).
- **SMARCD2, BCL7C, SS18L1** amplified in **6–8%** of breast cancers (TCGA/METABRIC).
- **CHD7** amplified in **~11%** of breast cancer patients; more prevalent in aggressive subtypes.
- **CHD3** heterozygous loss in **~60%**; **CHD9** in **~55%** (Chu et al., 2017).
- INO80 complex subunits altered in **~5%** overall; expression **downregulated in basal-type** breast cancer with worse OS/DMFS/RFS when low (Thang et al., 2023).
- Low **INO80** copy number more frequent in **TNBC** vs luminal/HER2+ (Thang et al., 2023).

---

## Key Quotes

> "Based on their structure and biochemical properties, chromatin remodeling complexes are divided into four subfamilies: SWI/SNF, ISWI, CHD and INO80."

> "Around 20% of all cancers possess mutations in the genes encoding SWI/SNF subunits."

> "Contrary to the tumor suppressive role of the SWI/SNF complex, the ATPase subunits of the SWI/SNF complex, BRM and BRG1, are highly expressed in primary breast cancer compared to normal breast tissue and are vital for cell proliferation."

> "A clinicopathological analysis also revealed that 78% of TNBCs exhibit low ARID1A expression, and breast cancer with low ARID1A mRNA expression is associated with advanced tumors, increased p53 expression, and high Ki-67 expression."

> "ARID1A-mutated tumours may depend on ARID1B for proliferation, suggesting a synthetic lethality combination between ARID1A and ARID1B and thus providing an opportunity for personalised targeting of cancer growth."

> "Depletion of CHD4 significantly decreases cell proliferation and migration in HER2-positive and triple-negative breast cancer cell lines, leading to a reduction in tumor mass in luminal B and HER2-ortholog-activated triple-negative PDX and transgenic mouse models."

> "Low INO80 copy number status is also associated with an increased risk in TNBC patients compared to luminal and HER2+ patients."

> "While SWI/SNF is overall considered a tumor suppressor, some members of the subfamily possess dual roles as tumor suppressors and oncogenes in certain cancers, but the mechanism underlying this context-specific function is unknown."

> "Several breast cancer cell lines, such as MCF7, MDA-MB-486, and MDA-MB-231, exhibit resistance to AU15330 treatment."

> "Research avenues must also explore the possibility of exploiting the chromatin remodeling complexes as measurable endpoint biomarkers for predicting therapeutic response and prognosis in breast cancer."

---

## Cross-References

### Complements entries in corpus

- **`davies_2017_hrdetect`**: ARID1A participates in DNA end resection and PARP sensitivity (review cites ARID1A-deficient cancers responding to PARP inhibitors); links A5 SWI/SNF loss to A1 HRD/DNA-repair vulnerability classes.
- **`telli_2016_hrd_score`**: Parallel DNA-repair deficiency framing — remodeler-mediated repair defects (ARID1A, CHD4–PARP) may co-segregate with HRD scars detectable by complementary methods.

### Contradicts / Tensions

- **Internal tension (same review):** Complex-level SWI/SNF labeled tumor suppressor while BRG1/BRM ATPases classified oncogenic in breast — agents must not treat "SWI/SNF mutation" as uniformly loss-of-function without subunit resolution.
- **`davies_2017_hrdetect`**: HRDetect targets biallelic BRCA1/BRCA2 deficiency; this review emphasizes BRG1–BRCA1–TP53 cooperation but does not establish that SWI/SNF alterations substitute for HRDetect features on WES.

### Cross-corpus connections

- **`B_Therapeutic_Context`**: BRG1 depletion increases chemotherapy sensitivity via ABC transporter downregulation (paclitaxel, 5-FU); ARID1A loss mediates endocrine resistance (tamoxifen, fulvestrant); BPTF/NURF linked to immune checkpoint escape — maps A5 genes to neoadjuvant drug classes.
- **`C_Cancer_Subtype`**: TNBC enrichment (ARID1A low expression, ARID1B high, INO80 low copy number); HER2+ CHD4/PI3K axis; ER+ ARID1A/endocrine resistance — gates which remodeler signals apply to the project's TNBC/HER2+ focus.
- **`D_Clinical_Endpoint`**: Review endpoints are OS, RFS, DMFS, relapse, treatment response — softer than pCR; use only as secondary evidence until pCR-linked studies are ingested.
- **`E_Study_Type`**: When primary neoadjuvant WES cohort papers appear, classify as cohort/trial evidence to upgrade genes currently supported only by this review.

### Related entries to add

- **HIGH:** Primary WES/neoadjuvant studies associating **ARID1A**, **SMARCA4**, **PBRM1** mutations with pCR or residual disease in TNBC/HER2+.
- **HIGH:** **Nagarajan et al. 2020** (ARID1A endocrine resistance) and **Thang et al. 2023** (INO80 basal breast cancer) as decision sources if neoadjuvant relevance emerges.
- **MEDIUM:** **CHD4** HER2/TNBC functional papers (D'Alesio et al.) for mechanism depth beyond this review.
- **LOW:** Non-breast SWI/SNF inhibitor clinical trials (FHD-286) unless breast expansion cohorts are published.

---

## Author Notes

### Priority justification

**MEDIUM** priority and **relevance_score 3** — useful background gene catalog for A5 and AQ-3 noise filtering, but review format, progression/resistance endpoints, and absence of pCR data limit its weight relative to decision sources in A1/A4.

### Use this source for

- Listing which chromatin-remodeling **genes and complexes** have breast-cancer literature support
- Initial **oncogenic vs tumor-suppressive** tagging of A5 candidates before pCR validation
- Understanding **subtype-specific** remodeler biology (TNBC ARID1A/ARID1B; basal INO80; HER2+ CHD4)
- Mapping **synthetic lethality and drug-sensitization** hypotheses (ARID1A→PARP; ARID1A↔ARID1B; CHD4–PARP)
- Identifying **cross-family structure** (BAF/PBAF/ncBAF, NuRD, p400/TIP60) for feature-class definitions

### Do NOT use this source for

- **pCR effect sizes or neoadjuvant response rates** → requires `D_Clinical_Endpoint` primary cohorts
- **Definitive AQ-3 driver ranking** → dual-role genes and review-level evidence insufficient alone
- **Clinical treatment recommendations** → therapeutic sections are largely preclinical/extrapolated
- **WES detection algorithms** → route to `E_Study_Type` methods papers

### Curation notes

- Harmonize gene symbols: BRG1=`SMARCA4`, BRM=`SMARCA2`, UCH37=`UCHL5`, YL1=`VPS72`.
- Index candidate genes under Concepts → "Chromatin remodeling / epigenetic regulators" and AQ-3.
- Flag **CHD4** and **BRG1/BRM** for dual-role metadata in future index tension table.
- Gap: no mention of neoadjuvant pCR — prioritize ingesting empirical TNBC/HER2+ WES response studies.

---

## Related Concepts

SWI/SNF, BAF, PBAF, ncBAF, ISWI, NURF, CHD, NuRD, INO80, p400/TIP60, H2A.Z, ATP-dependent remodeling, ARID1A, ARID1B, ARID2, SMARCA4, SMARCA2, PBRM1, SMARCB1, SMARCC1, SMARCD2, BPTF, SMARCA5, CECR2, CHD1, CHD4, CHD5, CHD7, INO80, SRCAP, UCHL5, synthetic lethality, PARP inhibitor, endocrine resistance, TNBC, HER2-enriched, EMT, DNA repair, immune escape, PROTAC, bromodomain inhibitor

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
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated *(deferred per ingestion constraints — suggestions returned separately)*
- [ ] the corpus `README.md` registry and counts have been updated *(deferred per ingestion constraints — one-line description returned separately)*
