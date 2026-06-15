---
name: corpus-driven-ideation
description: Produce structured corpus landscape reports that surface mandatory foundations, open choices, idea chains, surprises, and gaps from a single corpus, grounded in the project's goals. Used by corpus experts during ideation cycles.
---

# Corpus-Driven Ideation — Landscape Protocol

## When to Use

Use this skill when an expert agent must produce a structured **landscape report** for their corpus during an ideation cycle — surfacing what the corpus is saying about the project's anchor questions, where the real choices are, and where the surprises and gaps lie.

The expert produces a **landscape analysis**, not a ranked idea menu. Downstream, `consultant_cross_domain` assembles these landscape reports into complete research paths, and `skeptical_reviewer` enriches and pressure-tests them.

## Design Philosophy

The protocol asks the expert: **"What does my corpus actually say about the project's anchor questions, where are the real disagreements, and what is missing?"**

- experts produce landscape analyses anchored in `Doc/Project_description/project_overview.md`
- each item is **grounded in concrete paper_ids**, not generic field knowledge
- the report concludes with concrete curation consequences (gaps, sources to add)

## Who Can Use This Skill

- any corpus expert (`expert_<corpus>`)
- `consultant_cross_domain` (when synthesizing across corpora)

## Prerequisites

Before running ideation, the agent must have read:

1. Their own `CROSS_REFERENCE_INDEX.md` (full read, not sampling)
2. Their own `enriched_cross_reference_index/` if it exists
3. `Doc/Project_description/project_overview.md` (the corpus's scope and the anchor questions)

## Procedure

### Step 1 — Corpus deep scan

Read the index systematically. For each major section, ask: which entries are most relevant to the anchor questions? what has not been connected to them? what contradictions exist? what gaps would change the landscape if filled? what combinations across sections have not been considered together?

### Step 2 — Project grounding

For each observation, check against the anchor questions in `project_overview.md`: does this engage an anchor question? is it in scope? does it open a bridge to another corpus?

### Step 3 — Cross-pollination check

Consider adjacent areas not yet in the corpus, and bridges to other corpora.

### Step 4 — Produce the landscape report

Use the format below. Do **not** rank items competitively; describe the landscape the corpus sees.

## Output Format

```text
---
CORPUS LANDSCAPE REPORT

Expert: [agent name]
Date: [date]
Corpus: [corpus name and path]
Scope: [full corpus / targeted area]
Sources consulted: [README, index, enriched layer, specific paper_ids, project_overview sections]

---

## 1. Mandatory Foundations
Concepts any informed treatment of the anchor questions must include.
### MF-1: [Title]
**What it is**: ...
**Why mandatory**: ...
**Corpus grounding**: [paper_ids, index sections]
**Anchor question engaged**: ...
[typically 3-6]

## 2. Open Choices
Where the corpus contains real alternatives requiring an explicit choice.
### OC-1: [Title]
**The choice**: ...
**Alternative A**: [+ paper_ids + arguments]
**Alternative B**: [+ paper_ids + arguments]
**What would resolve it**: ...
**Project implication**: ...
[typically 2-5]

## 3. Idea Chains
Lineages worth tracing (source A enables B enables C, with paper_ids).

## 4. Surprises and Cross-Pollination
### SR-1: [Title]
**The connection**: ...
**Sources involved**: [paper_ids]
**Bridge corpus** (if any): ...
**Why it matters**: [anchor question]

## 5. Corpus Gaps Identified
Concrete gaps that would change the landscape if filled.

## 6. Cross-Corpus Dependencies
Where this analysis would benefit from another corpus expert.
---
```

## Quality Criteria

A landscape report is not complete unless it: contains at least 3 mandatory foundations grounded in concrete paper_ids; contains at least 2 genuine open choices (not false choices); grounds every item in specific corpus sections and paper_ids; connects every item to at least one anchor question; names at least 2 corpus gaps; names at least 1 cross-corpus dependency.

## What This Skill Does NOT Do

- it does not produce ranked idea menus
- it does not replace `consultant_cross_domain` for path synthesis
- it does not produce final proposals (that is `model_creator`)
