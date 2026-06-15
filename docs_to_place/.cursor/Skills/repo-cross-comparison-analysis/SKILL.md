---
name: repo-cross-comparison-analysis
description: Build structured cross-comparison documents that synthesize how multiple repositories (and their papers) approach the same design problem, leading to a project-grounded recommendation. Use when a design choice has several viable approaches visible across codebases and a decision must be made.
---

# Repository Cross-Comparison Analysis

## Purpose

This skill creates **structured comparison documents** that synthesize how multiple codebases solve the same design problem, ending in a grounded recommendation for **this project**.

It is distinct from `repo-ingestion` (which extracts knowledge from a single repo) and from `corpus-enrichment-analysis` (which maps idea chains within a literature corpus). This skill is for **decision support**.

## When to Use

- A design decision has **three or more** comparable approaches across repos.
- A newly ingested repo adds a data point to an existing comparison.
- The user or an orchestrator asks for a comparison to settle a specific choice.

## Required Inputs

Before writing, read: all relevant `EXTRACT_*.md` files in `Doc/Corpus/code_repos/repos_md/`; the corresponding corpus summaries; existing comparisons in `Doc/Corpus/code_repos/cross_comparisons/` (to avoid duplication and to cross-link); `HYPERPARAMETER_ATLAS.md`; and `Doc/Project_description/project_overview.md` (for the project constraints the comparison must respect).

## Document Structure

Files go in `Doc/Corpus/code_repos/cross_comparisons/` as `CROSS_COMPARISON_{topic}.md` (lowercase, underscores; named for the comparison axis, not the conclusion).

```markdown
# Cross-Comparison: {Topic}
> Informs: {which decision} | Sources: {repo1, repo2, repo3, ...}
> Updated: {date} — {change note if updating}

## Approaches Compared
| Approach | Source | Mechanism | Scale validated | Fits this project? |
|---|---|---|---|---|

## Key Differences
### {Axis 1}
- Repo A: ... (with code reference)
- Repo B: ...

## Detailed Mechanisms
### {Approach} ({Source})
```code
# file:line reference to the source repo
```
Key insight: ...

## Analysis for This Project
- Assumption audit: which assumptions hold here, which break.
- Scale sensitivity: does it work at this project's data scale?
- Compatibility: inputs, constraints, environment.
- Robustness / interpretability / compute budget as relevant.

## Recommendation
### Primary choice
{with justification}
### Comparison / ablation strategy
{what to test, in what order}
### Fallback
{what to try if the primary choice fails, and the trigger to switch}
```

## Analysis Dimensions

Evaluate every comparison along: (1) mechanism, (2) assumption audit, (3) scale sensitivity, (4) input/constraint compatibility, (5) robustness to missing or noisy data, (6) interpretability, (7) computational budget. Drop dimensions that are irrelevant to the project, but state that you did.

## Quality Standard

A comparison is complete only when it: compares ≥3 approaches with code-grounded evidence; gives each approach at least one attributed code snippet; analyses the approaches against this project's constraints; states a clear recommendation with rationale; proposes an ablation strategy; defines a fallback with a switch trigger; and cross-links related comparisons.

## Do Not Do

- Do not compare approaches without reading the actual code, not just the paper.
- Do not recommend without grounding in this project's constraints.
- Do not write a comparison with only two approaches (use inline notes in the EXTRACT files instead).
- Do not omit the fallback — every recommendation needs an escape hatch.
- Do not duplicate EXTRACT content; reference it.
