---
name: ingest_article
description: Process sources (papers, books, essays, technical reports, web pages) into structured corpus entries, update CROSS_REFERENCE_INDEX.md, and update the corpus README. Use when adding any source to a corpus.
---

# Article Ingestion

## Purpose

This skill defines the reusable corpus-building procedure for the knowledge system. It is the single canonical way to turn a raw source into indexed, reusable knowledge.

## Core Principle

A corpus is not a passive archive. It is a reasoning system. Every curated entry must help an expert agent answer questions through indexed knowledge rather than raw documents.

## Required References

Before curating a new source, read these files in order:

1. `Doc/Corpus/HOW_TO_ADD_PAPERS.md` — the **authoritative ingestion guide** (metadata guidance, the 6 critical improvements, the deep-ingestion protocol, verification checklist, common pitfalls)
2. `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md` — the single entry template for every corpus
3. `Doc/Project_description/project_overview.md` — to ground the relevance section
4. the destination corpus `README.md`
5. the destination corpus `CROSS_REFERENCE_INDEX.md`

`HOW_TO_ADD_PAPERS.md` is the single source of truth for ingestion quality. This skill file defines the agent workflow and output format; `HOW_TO_ADD_PAPERS.md` defines the substance.

## Supported Destinations

Any corpus directory under `Doc/Corpus/`. Each project defines its own corpora in `Doc/Project_description/project_overview.md`; this skill is corpus-agnostic.

## Workflow

Follow the 9-step procedure defined in `HOW_TO_ADD_PAPERS.md`:

1. **Add source** — rename to a canonical filename, place in the correct corpus category folder
2. **Choose destination** — select the corpus where the source is most useful as a reasoning object
3. **Create markdown summary** — use `PAPER_TEMPLATE_GENERAL.md`
4. **Fill metadata** — `corpus_role`, `temporal_status`, `relevance_score`, `priority_level`
5. **Apply the 6 critical improvements** — precise terminology, explicit assumptions, source-type contextualization, quantitative/qualitative specifics, direct quotes, cross-references
6. **Update CROSS_REFERENCE_INDEX.md** — add the source under relevant concepts, methods, open questions, contradictions, and hub entries
7. **Update corpus README.md** — add to the registry, increment the category count and total count
8. **Verify project relevance** — run the checklist in `HOW_TO_ADD_PAPERS.md` Step 8
9. **Retrieval check** — confirm the source is findable by paper_id, by concept, and by project relevance

For **decision sources**, follow the deep-ingestion protocol in `HOW_TO_ADD_PAPERS.md` Step 4b: read the actual document, fill all template sections from its content, and extract quotes, effect sizes, theorem scope, or canonical examples as appropriate.

## Output Format

After completing the ingestion, report:

1. `Destination` — which corpus and category
2. `Entry Created or Updated` — paper_id and file path
3. `Index Sections Updated` — which `CROSS_REFERENCE_INDEX.md` sections were changed
4. `README Registry Updated` — paper_id added, counts incremented
5. `New Gaps / Redundancies / Links` — what the ingestion revealed about the corpus
6. `Next Recommended Curation Action` — what should be ingested or updated next

## Rules

- Avoid duplicates.
- Preserve naming consistency within each corpus.
- A source is not fully ingested until the document has been renamed and co-located with its markdown summary in the final category folder.
- Use markdown summaries and indices as the primary reasoning interface.
- If the index is insufficient for reliable reasoning, improve the index rather than bypassing it.
- Prefer precise, reusable knowledge over vague summary.
- The project-relevance section (`Relationship with the project's goals`) is mandatory in every entry.
