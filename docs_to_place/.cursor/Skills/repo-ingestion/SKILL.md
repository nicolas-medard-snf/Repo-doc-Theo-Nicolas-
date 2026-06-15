---
name: repo-ingestion
description: Extract structured, traceable knowledge from a code repository and record it as reusable extraction files plus an implementation reference. Use when an expert must deeply read a codebase to capture reusable architectural patterns, configuration, training/evaluation recipes, and design decisions for the project.
---

# Repository Ingestion

## Purpose

This skill defines the reusable procedure for ingesting a code repository into the project's **implementation knowledge base** (`Doc/Corpus/code_repos/`).

It is the code-side counterpart to article ingestion. Where article ingestion turns a document into a structured summary and updates a `CROSS_REFERENCE_INDEX.md`, this skill turns a codebase into structured extraction files and an implementation reference.

## Core Principle

A repository is **a knowledge source to consult, not a dependency to import.**

Every extracted pattern must:

1. Be traceable to a specific file and line range in the source repository.
2. Be connected to the rationale that explains *why* it works (a corpus entry, a paper, or the repo's own documentation).
3. Be evaluated for applicability to **this project's** data, constraints, and goals before adoption.
4. Record where the source context diverges from this project and what adaptations are required.

## Required References

Before ingesting a repository, read:

1. `Doc/Corpus/code_repos/CODE_REFERENCES.md` — to check whether the repo is already tracked and at what tier.
2. `Doc/Corpus/code_repos/HYPERPARAMETER_ATLAS.md` — to see which configuration columns already exist.
3. `Doc/Corpus/code_repos/IMPLEMENTATION_COOKBOOK.md` — to see which recipes exist and where the new repo fits.
4. Any corpus summary already written for the method this repo implements.
5. `Doc/Project_description/project_overview.md` — to understand which goals and open questions the repo could inform.

> If the `code_repos/` corpus does not exist yet, create it like any other corpus (see `Doc/Corpus/README.md`), with a `README.md` registry and the reference files named above.

## Tier Assignment

Assign each repository to a priority tier reflecting how directly it serves the project:

| Tier | Meaning |
|------|---------|
| **Tier 1** | Directly reusable — core pipeline components you intend to adapt. |
| **Tier 2** | Component-level reference — a specific module, mechanism, or technique. |
| **Tier 3** | Baseline / evaluation reference. |
| **Tier 4** | Adjacent inspiration — a method from another context that may transfer. |

## Workflow

### Step 1 — Reconnaissance

Clone or browse the repo. Identify entry points, core logic, configuration system, data handling, the main loop, and evaluation. Record the structure as a tree.

### Step 2 — Deep extraction

Create `Doc/Corpus/code_repos/repos_md/EXTRACT_{REPO_NAME}.md`:

```markdown
# Extraction: {Repo Name}
> Extracted: {date} | Repo: {URL} | Commit: {hash or HEAD}
> Priority: {tier} — {one-line justification}

## Architecture
- Core structures and key design choices.

## Key Mechanisms
- The distinctive algorithmic contributions, with code snippets.

## Configuration / Hyperparameters
- Values from config files, with file references.

## Main Loop
- Step-by-step flow; optimizer / schedule / control logic.

## Data Handling
- Inputs, preprocessing, edge-case and missing-data handling.

## Evaluation
- Metrics, protocols, validation strategy.

## Adaptation Notes for This Project
- What can be used as-is; what must change; where assumptions diverge.
```

**Code citation rule:** every snippet is a fenced code block whose first line is a comment with the relative path and line range, e.g. `# path/to/file.py:42-58`. No anonymous snippets.

### Step 3 — Update the implementation reference

- Add or update the repo's configuration in `HYPERPARAMETER_ATLAS.md` (always include a "This-project default" column with a reasoned starting point and a rationale column).
- Add the repo to the relevant recipe in `IMPLEMENTATION_COOKBOOK.md`, or create a new recipe if it introduces a pattern not yet covered.
- Add or update the repo card in `CODE_REFERENCES.md` (tier, summary, what it provides, which decisions it informs, key files to read first).

### Step 4 — Record gaps and links

End the extraction with **Gaps** (what is still missing), **Links** (to related repos and corpus entries), and **Next** (recommended follow-up).

## Quality Standard

An ingestion is complete only when: an `EXTRACT_*.md` exists; the repo appears in `CODE_REFERENCES.md` with a tier and card; its configuration is in `HYPERPARAMETER_ATLAS.md`; at least one cookbook recipe references it; and the adaptation notes are specific, not generic.

## Do Not Do

- Do not copy code without attribution and a file:line reference.
- Do not register a repo without reading at least its core logic and main loop.
- Do not assume a pattern transfers to this project without checking the source's assumptions.
- Do not record only *what* the code does — capture *why* it works.
