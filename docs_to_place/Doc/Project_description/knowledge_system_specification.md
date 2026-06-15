# Knowledge System Specification

**Purpose**: this document specifies the **knowledge system** of the project. It defines, in a human-readable and persistent form:

- how knowledge is organized in this repository
- how corpora should be structured
- how `CROSS_REFERENCE_INDEX.md` files must function
- how expert agents are expected to read, maintain, and extend the knowledge base

This is a system-specification document, not an agent prompt and not a code specification.

---

## 1. Core Design Principle

The system is designed around one principle:

**reasoning should happen through structured, indexed knowledge rather than through raw documents or ad hoc memory.**

This means:

1. corpora are not passive archives
2. each corpus must be navigable through a `CROSS_REFERENCE_INDEX.md`
3. source-level markdown files are preferred over raw PDFs or extracted text
4. expert agents reason through curated abstractions first
5. gaps in indexing are treated as infrastructure problems to be reported and eventually fixed

---

## 2. Knowledge Layers

### 2.1 Project Overview Layer

Core file: `Doc/Project_description/project_overview.md`

Purpose: anchor reasoning in the project's actual goals rather than generic discipline definitions; define the scope, boundaries, and implicit questions of each corpus; prevent agents from drifting into encyclopaedic surveys disconnected from why each corpus exists.

This file is the **shared context layer** for every expert. It is small but mandatory.

### 2.2 The Corpora

Each project defines its own set of corpora in `Doc/Project_description/project_overview.md`. There is no fixed number; create as many as the project's domains require.

Each corpus is owned by a dedicated specialization of the corpus-expert template (one expert per corpus).

Each corpus contains, at minimum:

- `README.md` — registry, category counts, scope
- `CROSS_REFERENCE_INDEX.md` — primary navigation interface
- one folder per sub-domain (created as the corpus grows)
- `enriched_cross_reference_index/` — added once the corpus is large enough to benefit from second-order analysis

### 2.3 Cross-Corpus Bridge Layer

Location: `Doc/Hypotheses/cross_corpus_enriched_cross_reference_index/`

Purpose: map transfer chains, bridge mechanisms, tensions, and project consequences **across** two corpora; explain how upstream ideas in one corpus become relevant through another; persist evolving cross-corpus understanding in reviewable, incremental documents.

Produced by the `cross-corpus-enrichment-analysis` skill. The dominant/secondary corpus asymmetry is always explicit.

---

## 3. Role of `CROSS_REFERENCE_INDEX.md`

Every corpus must expose a `CROSS_REFERENCE_INDEX.md` — the **primary reasoning interface** of the corpus.

### 3.1 Why the Index Exists

It should make it possible to answer: which entries are relevant to this concept? what methods already address this question? where are the contradictions? which entries are hubs? what is missing? what link between topics has not yet been explored?

### 3.2 Mandatory Behavior for Experts

When using an owned corpus, an expert agent should: (1) start with `CROSS_REFERENCE_INDEX.md`; (2) identify the relevant section(s); (3) follow mapped links to targeted markdown entries; (4) reason from the indexed structure and targeted entries; (5) explicitly report when the index is insufficient.

### 3.3 Progressive Knowledge Access

1. **Layer 1 — Primary index** (`CROSS_REFERENCE_INDEX.md`): first stop for every substantive task
2. **Layer 2 — Enriched corpus layer** (`enriched_cross_reference_index/`): consulted when the task needs second-order structure
3. **Layer 3 — Cross-corpus bridge layer** (`Doc/Hypotheses/cross_corpus_enriched_cross_reference_index/`): consulted when the task spans two corpora

Each layer builds on the previous one without replacing it. Experts must never bypass Layer 1 when it exists.

### 3.4 What the Index Must Support

A mature index should contain: concepts → entries; methods / mechanisms / schools of thought → entries; open questions → entries; contradictions / tensions; hub entries; important negative findings or rejected ideas; unexplored combinations; gaps that require curation.

### 3.5 What the Index Must Not Become

A giant unordered note dump; a duplicate of every summary; a static artifact that stops evolving. Its role is navigation, synthesis, and reasoning support.

---

## 4. Corpus Entry Standard

Every curated entry is a markdown file using `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`. The template is single and generic, with optional domain-flavored sections the expert fills only when relevant.

### 4.1 Required Structure

`Key Contributions`; `Core Idea / Mechanism / Argument`; `Methodology / Evidence Base`; `Relationship with the project's goals` (mandatory bridge); `Assumptions`; `Limitations / Failure Modes`; `Key Quantitative or Qualitative Results`; `Key Quotes`; `Cross-References`; `Author Notes`; `Related Concepts`.

### 4.2 Corpus Roles and Temporal Status

Every entry carries two YAML fields:

- `corpus_role`: **`decision`** (entry whose claims/methods/framework you would actively build from, reuse, or test against — the primary surface for ideation and synthesis) or **`reference`** (review, survey, foundation, background — supports framing, not direct adoption).
- `temporal_status`: **`active_candidate`** (current work or older work still standard) or **`historical_pedagogical`** (superseded by newer work in the corpus).

Expert agents **prioritize decision-corpus entries** when answering substantive questions. The `corpus-driven-ideation` skill (if installed) focuses its deep scan on decision-corpus entries.

---

## 5. Ownership Model

The knowledge system is explicitly tied to expert ownership.

**Ownership means** the expert is responsible for: using the owned corpus as the primary reasoning surface; maintaining an internal map of concepts and relationships; noticing gaps and redundancies; surfacing contradictions; suggesting curation when the corpus is insufficient.

**Ownership does not mean exclusive access**: other agents may consult the corpus, but the owner remains the primary interpreter and maintainer of that domain.

Each corpus maps to one expert agent file `.cursor/Agents/expert_<short_name>.md`, all instances of the same template `.cursor/Agents/expert_corpus_template.md`.

---

## 6. Maintenance Workflow and Skill Ecosystem

| Skill | Location | Purpose |
|-------|----------|---------|
| Article Ingestion | `.cursor/Skills/ingest_article/SKILL.md` | Add new sources: rename, markdown summary, index update, README registry update |
| PDF Annotation | `.cursor/Skills/pdf_annotation/SKILL.md` | Deep-read and annotate a PDF with structured highlights |
| Corpus Enrichment | `.cursor/Skills/corpus-enrichment-analysis/SKILL.md` | Build a second-order analysis layer over one corpus |
| Cross-Corpus Enrichment | `.cursor/Skills/cross-corpus-enrichment-analysis/SKILL.md` | Build a second-order bridge layer across two corpora |
| MD Navigator | `.cursor/Skills/md-navigator/SKILL.md` | Generate browsable HTML navigators |
| MD to PDF | `.cursor/Skills/md-to-pdf/SKILL.md` | Convert markdown to print-ready PDFs |

Each corpus `README.md` serves as the **authoritative registry**: a Corpus Categories table with per-category counts and a total, and a Full Registry listing every `paper_id` with a one-line description. A source is not fully ingested until it appears in the registry.

If the index is too weak to support reliable expert reasoning, the correct action is to improve the index through curation — not to bypass the indexed system and treat raw documents as the normal interface.

---

## 7. Failure Modes the System Is Designed to Prevent

| Failure mode | How prevented |
|---|---|
| Generic, unanchored reasoning | Corpus ownership, required shared overview, index-first reasoning |
| Repeated reinvention | Curated markdown entries, contradiction tracking, gap detection, persistent agent memory |
| Overlap between experts | Explicit ownership of corpora, corpus-specific reasoning interfaces |
| Drift away from project intent | Stable `project_overview.md`, mandatory bridge section in every entry |
| Raw-document dependence | Markdown-first entry structure, `CROSS_REFERENCE_INDEX.md` as primary interface |

---

## 8. Summary

This system makes a knowledge base reason like a structured curation organization. Core commitments: knowledge organized into explicit corpora with structured indices; each corpus navigated through `CROSS_REFERENCE_INDEX.md`, deepened by enriched layers, and bridged across corpora; experts own domains rather than answering generically; curation, enrichment, and annotation are part of the infrastructure, supported by reusable skills.
