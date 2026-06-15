# Corpus

This directory holds the project's corpora. Each corpus is a curated, indexed body of knowledge owned by one expert agent.

## How the corpora are organized

```
Doc/Corpus/
├── README.md                       ← this file
├── HOW_TO_ADD_PAPERS.md            ← authoritative ingestion guide
├── PAPER_TEMPLATE_GENERAL.md       ← the single entry template
├── _templates/                     ← skeletons for a new corpus
│   ├── CORPUS_README_TEMPLATE.md
│   └── CROSS_REFERENCE_INDEX_TEMPLATE.md
└── <your_corpus>/                  ← one folder per corpus
    ├── README.md                   ← registry + category counts + scope
    ├── CROSS_REFERENCE_INDEX.md    ← primary reasoning interface
    ├── <category>/                 ← entries grouped by sub-domain
    └── enriched_cross_reference_index/   ← second-order analysis (added later)
```

## Reasoning interface

Agents reason **through the indices first**, not through raw documents:

1. **Layer 1** — `CROSS_REFERENCE_INDEX.md` (per corpus): the primary navigation surface
2. **Layer 2** — `enriched_cross_reference_index/` (per corpus): second-order structure
3. **Layer 3** — `Doc/Hypotheses/cross_corpus_enriched_cross_reference_index/`: cross-corpus bridges

## Creating a new corpus

1. Decide the corpus and add it to `Doc/Project_description/project_overview.md`.
2. Create `Doc/Corpus/<your_corpus>/` and copy the two files from `_templates/` into it as `README.md` and `CROSS_REFERENCE_INDEX.md`.
3. Instantiate its expert: copy `.cursor/Agents/expert_corpus_template.md` to `.cursor/Agents/expert_<short_name>.md` and fill the placeholders.
4. Create the memory shell `.cursor/agents_memory/expert_<short_name>_memory.md`.
5. Start ingesting with the `ingest_article` skill.

## Adding sources

See `HOW_TO_ADD_PAPERS.md`. Every entry uses `PAPER_TEMPLATE_GENERAL.md` and must include the mandatory `Relationship with the project's goals` section.
