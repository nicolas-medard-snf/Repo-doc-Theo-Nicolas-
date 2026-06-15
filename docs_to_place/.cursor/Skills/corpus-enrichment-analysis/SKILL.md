---
name: corpus-enrichment-analysis
description: Build an enriched analysis layer on top of a corpus CROSS_REFERENCE_INDEX.md, README.md, curated markdown summaries, and selected raw sources. Use when an expert must deepen a corpus by mapping idea chains, bridge sources, tensions, trend lines, and curation priorities into an incremental enriched_cross_reference_index/ document.
---

# Corpus Enrichment Analysis

## Purpose

This skill creates a **second-order reasoning layer** over an existing corpus.

It is distinct from:

- `ingest_article`: adds or updates entries and the primary index
- `corpus-driven-ideation` (if installed): generates landscape reports from the corpus

This skill is for **understanding the internal structure of the corpus itself**:

- how ideas evolve across sources
- which sources act as bridges or bottlenecks
- where the corpus contains tensions, hidden alignments, or incomplete chains
- what the corpus is starting to imply before any landscape report is written

## When to Use

- the user asks to enrich a corpus index or README
- an expert needs a deeper map of relationships between concepts, sources, and mechanisms
- the corpus has grown enough that the primary `CROSS_REFERENCE_INDEX.md` is no longer sufficient
- you want an incremental, persistent record of how expert understanding of a corpus evolves over time

## Default Scope

Apply to **one owned corpus at a time** (any corpus directory under `Doc/Corpus/`).

## Required Inputs

Before writing an enriched document, read:

1. `Doc/Project_description/knowledge_system_specification.md`
2. `Doc/Project_description/project_overview.md`
3. the corpus `README.md`
4. the corpus `CROSS_REFERENCE_INDEX.md`
5. previous reports in the corpus `enriched_cross_reference_index/` folder, if they exist
6. the most relevant markdown summaries for hub sources, bridge sources, contradictions, and recent additions
7. selected raw sources for validation

Use raw-source grounding strategically: for hub sources, summarisation-compressed nuance, contradictions, and recent or high-impact sources.

## Core Principle

The enriched layer must **sit above** the primary index, not replace it. The primary `CROSS_REFERENCE_INDEX.md` remains the main navigation interface; the enriched layer explains the **deeper logic** of the corpus.

## Workflow

### Step 1: Read the primary reasoning surface

Start with `CROSS_REFERENCE_INDEX.md` and `README.md`. Extract: major concept/mechanism families, anchor-question mappings, idea clusters, hub sources, contradictions, and known gaps.

If previous enrichment passes exist, read them before drafting the next one. Make new passes incremental, not repetitive: preserve stable findings unless new evidence changes them, deepen one or two additional lenses, and explicitly refine earlier interpretations when justified.

### Step 2: Build the second-order map

Across the index and summaries, identify:

- **idea chains**: source A enables source B enables source C
- **bridge sources**: one source connects otherwise separate clusters
- **compression sources**: one source turns a broad area into a reusable pattern
- **turning points**: sources that change the dominant framing of a problem
- **project anchors**: sources with unusually direct relevance to the project goals

### Step 3: Validate against summaries

Read the markdown summaries for the most important sources in each chain. Look for core idea/mechanism wording, assumptions, failure modes, explicit relationship sections, and existing cross-references.

### Step 4: Validate against raw sources

Read selected raw sources to verify that the claimed turning point or tension is real and not only curator interpretation.

### Step 5: Write the enriched layer

Create or update a document in `<CORPUS_PATH>/enriched_cross_reference_index/`. Naming convention: `cross_reference_index_enriched_1_time.md`, `cross_reference_index_enriched_2_time.md`, etc.

### Step 6: End with curation consequences

Conclude with: high-value gaps, weak links in the existing index, candidates to add to the primary index, candidates to add to the README registry, and sources or clusters that would deserve a later meta-analysis.

## Analysis Lenses

Cover most of these per pass:

1. **Genealogy** — which lineages matter most, which older sources remain structurally active
2. **Bridge Logic** — which sources connect different sub-areas, which concepts recur under different names
3. **Tensions** — where strong lines of work pull in different directions
4. **Trend Lines** — directional movement visible across the corpus
5. **Project Consequences** — which corpus shifts matter immediately for the project goals
6. **Curation Consequences** — what is missing that would complete a chain

## Output Structure

```markdown
# Enriched Cross-Reference Index — [Corpus Name]

## Purpose of this enrichment pass
## Sources consulted
## Corpus state snapshot
## High-order idea chains
## Bridge sources and hub sources
## Deepened tensions and contradictions
## Trend lines
## Project consequences
## Curation priorities
## Candidate updates to the primary index / README
## Candidate sources or clusters for later meta-analysis
```

## Quality Standard

An enriched document is not complete unless it:

1. clearly differs from a normal index and from a landscape report
2. names concrete sources and concepts, not vague themes alone
3. distinguishes **observed in corpus** from **inferred by analysis**
4. uses selected raw-source grounding for at least some key claims
5. ends with actionable curation consequences
6. preserves the primary role of `CROSS_REFERENCE_INDEX.md`
7. identifies meta-analysis candidates when the corpus structure supports a meaningful comparison set

## Do Not Do

- merely rewrite the existing `CROSS_REFERENCE_INDEX.md`
- turn the enriched layer into a dump of source summaries
- skip the corpus `README.md`
- rely only on raw sources when curated markdown already exists
