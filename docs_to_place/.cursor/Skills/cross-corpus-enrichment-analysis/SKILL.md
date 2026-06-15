---
name: cross-corpus-enrichment-analysis
description: Build a second-order analysis layer across two corpora (one dominant, one secondary). Maps transfer chains, bridge sources, cross-corpus tensions, and joint consequences for the project goals into an incremental document under Doc/Hypotheses/cross_corpus_enriched_cross_reference_index/.
---

# Cross-Corpus Enrichment Analysis

## Purpose

This skill creates a **second-order cross-corpus reasoning layer**.

It is distinct from:

- `corpus-enrichment-analysis`: deepens one corpus at a time
- `corpus-driven-ideation` (if installed): generates landscape reports
- `ingest_article`: updates entries or main corpus indices

This skill is for understanding:

- how one corpus supplies upstream logic for another
- which concepts, sources, or interfaces bridge the corpora
- where tensions appear only when both corpora are read together
- what the two corpora jointly imply for the project goals

## When to Use

- the user asks for cross-corpus enrichment or synthesis
- an expert owns one dominant corpus but must reason with a secondary corpus
- the main insight lies in the relationship between corpora, not inside one alone
- you want a persistent record of how cross-corpus understanding evolves over time

## Core Model

Treat the two corpora **asymmetrically** unless the user says otherwise:

- **Dominant corpus**: the corpus that owns the main question
- **Secondary corpus**: the corpus that supplies upstream mechanisms, abstractions, or bridge logic

## Required Inputs

Before writing, read:

1. `Doc/Project_description/knowledge_system_specification.md`
2. `Doc/Project_description/project_overview.md` (focus on how the corpora relate)
3. dominant corpus `README.md`
4. dominant corpus `CROSS_REFERENCE_INDEX.md`
5. dominant corpus enriched layer if it exists
6. secondary corpus `README.md`
7. secondary corpus `CROSS_REFERENCE_INDEX.md`
8. secondary corpus enriched layer if it exists
9. previous reports in `Doc/Hypotheses/cross_corpus_enriched_cross_reference_index/` for the same corpus pair, if any
10. key markdown summaries for bridge sources, tensions, and project anchors from both corpora
11. selected raw sources from both corpora

## Core Principle

The cross-corpus layer **sits above** both primary corpus indices; it does not replace them.

## Workflow

### Step 1: Read the two primary reasoning surfaces

Extract: dominant-corpus mechanism families and anchor questions; secondary-corpus upstream mechanisms and abstractions; hub sources and contradictions in each; any enriched-layer findings already recorded.

If previous cross-corpus passes exist for the same pair, read them and make the new pass incremental.

### Step 2: Build the cross-corpus map

Identify:

- **transfer chains**: secondary source/mechanism → dominant source/family → project consequence
- **bridge sources**: entries that operationally connect the corpora
- **upstream/downstream pairs**: one corpus proposes a mechanism, the other makes it real for the project
- **cross-corpus tensions**: one corpus pushes one way, the other complicates it
- **project anchors**: sources with unusually direct relevance to the project goals

### Step 3: Validate against summaries

Read the most important markdown summaries from both corpora.

### Step 4: Validate against raw sources

Use selected raw sources to verify that bridge logic and tensions are real.

### Step 5: Write the cross-corpus layer

Create or update a document at `Doc/Hypotheses/cross_corpus_enriched_cross_reference_index/`. Naming convention: `cross_reference_index_<corpus1_short>_<corpus2_short>_enriched_1_time.md`, etc. Use corpus short identifiers, not agent names.

### Step 6: End with consequences

Conclude with: what the two corpora jointly imply for the project; which links deserve later reinforcement in the primary indices; what gaps would complete the cross-corpus chain; which sources or comparable source groups deserve later meta-analysis.

## Analysis Lenses

1. **Upstream → Downstream Logic**
2. **Bridge Logic**
3. **Cross-Corpus Tensions**
4. **Joint Trend Lines**
5. **Project Consequences**
6. **Curation Consequences**

## Output Structure

```markdown
# Cross-Corpus Enriched Cross-Reference Index — [Corpus 1] × [Corpus 2]

## Purpose of this enrichment pass
## Corpora and roles (dominant / secondary)
## Sources consulted
## Cross-corpus state snapshot
## Main transfer chains
## Bridge sources and bridge concepts
## Cross-corpus tensions
## Joint trend lines
## Consequences for the project goals
## Curation priorities
## Candidate updates to the primary indices / README files
## Candidate sources or clusters for later meta-analysis
```

## Quality Standard

A cross-corpus document is not complete unless it:

1. clearly differs from a single-corpus enrichment
2. makes the dominant/secondary asymmetry explicit
3. names concrete sources and concepts from both corpora
4. distinguishes **observed in corpus** from **inferred by analysis**
5. uses selected raw-source grounding from both corpora
6. ends with actionable consequences

## Do Not Do

- merely merge two existing enriched documents
- rewrite both primary indices
- ignore the dominant/secondary distinction unless the user explicitly asks for symmetry
