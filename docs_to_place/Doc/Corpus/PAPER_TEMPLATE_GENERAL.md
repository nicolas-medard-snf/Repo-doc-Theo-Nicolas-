# Source Summary Template — General

**Applies to**: every corpus under `Doc/Corpus/`.

Before using this template, read:

- `Doc/Corpus/HOW_TO_ADD_PAPERS.md`
- `Doc/Project_description/project_overview.md`
- the destination corpus `README.md`
- the destination corpus `CROSS_REFERENCE_INDEX.md`

This template supports **indexed reasoning grounded in the source**, not passive summarization. Discipline-specific sections (empirical study design, mathematical formalism, argument structure) are optional — fill only what is relevant for the source at hand.

---

## Metadata

```yaml
---
paper_id: "firstauthor_year_short_keyword"
title: "Full title"
authors: "Author 1, Author 2, Author 3"
year: 2023
venue: "Journal / Publisher / Conference / Web"
paper_type: "primary_research | review | survey | methodological | foundational | book | essay | field_report | manifesto | textbook"
domain: "<corpus short name>"
subdomain: "free-form short string identifying the sub-area"
relevance_score: 4
priority_level: "HIGH"
corpus_role: "decision | reference"
# corpus_role = "decision": source you would actively build from, reuse, cite as
#   primary support, or test against. Feeds the corpus-driven-ideation skill.
# corpus_role = "reference": review, survey, foundation, tangential method, or
#   background. Useful for framing, not for direct adoption.
temporal_status: "active_candidate | historical_pedagogical"
# temporal_status = "active_candidate": current work or older work still standard.
# temporal_status = "historical_pedagogical": important historically but
#   superseded by newer work in the corpus.
relevance_tags:
  - "tag_1"
  - "tag_2"
doi: ""
isbn: ""
url: ""
pdf_file: "firstauthor_year_short_keyword.pdf"
---
```

---

## One-Sentence Summary

State in one sentence what this source contributes and why it matters for the project's goals.

---

## Key Contributions

- Contribution 1
- Contribution 2
- Contribution 3

---

## Core Idea / Mechanism / Argument

Explain what the source actually claims, demonstrates, or proves.

Requirements:

- use the discipline's precise vocabulary (named concepts, named operations, named arguments)
- include equations, formal definitions, or argument structures where relevant
- explain the **information flow / argument flow** step by step, not as a marketing summary
- distinguish what is novel from what is inherited from prior work
- distinguish what is **claimed** from what is **demonstrated**

---

## Methodology / Evidence Base

Describe the operational basis of the source. Fill the sub-sections that apply.

### If empirical:
- **Design**: experimental / observational / longitudinal / cross-sectional / meta-analytic
- **Sample / setting**: N, demographics, context
- **Intervention or exposure** (if applicable)
- **Measurements / instruments**
- **Statistical analysis approach**
- **Replication or pre-registration status**

### If formal:
- **Definitions used**
- **Axioms or assumed framework**
- **Proof structure** (constructive, by contradiction, by induction, model-theoretic, etc.)
- **Theorem(s) and their scope**

### If conceptual / theoretical / synthesis:
- **Theoretical framework invoked**
- **Sources drawn upon**
- **Position in the existing debate**

### If methodological / applied / "how-to":
- **What the method does**
- **What it requires (inputs, skills, time)**
- **Where it has been used in practice**

---

## Relationship with the project's goals

> **Mandatory section**. Reference `Doc/Project_description/project_overview.md`.

### Which corpus scope and anchor question(s) this source engages with

- Corpus: ...
- Anchor question(s): ...
- Bridge corpus (if relevant): ...

### How it could be used

- **Directly reusable**: a concept, framework, technique, or evidence to invoke directly
- **Indirectly inspiring**: a pattern, vocabulary, or framing
- **Mainly background / framing**: contextualizes the problem space

Explain why, specifically.

### Main fit with the project

- What part of the source maps cleanly onto a question or pattern the project cares about?

### Main mismatch or risk

- Where does the source's setting differ from the project's context?
- Where is the evidence weaker than the claim?

### Concrete follow-up

- What should the agent do with this source next?
- Any cross-references to other corpora that should be added?

---

## Assumptions

State the assumptions explicitly (evidence-base representativeness, foundational framework, scope of generalization, prerequisite context, etc.).

---

## Limitations / Failure Modes

- Limitation 1
- Limitation 2

Be specific. Prefer real failure conditions over vague caveats.

---

## Key Quantitative or Qualitative Results

Fill the relevant variant (effect sizes and tables if empirical; exact theorem statements and scope if formal; canonical examples and counterexamples if conceptual).

---

## Key Quotes

Include 5–10 short direct quotes from the body that are genuinely useful for future grounding (define a mechanism, state a central claim with evidence, identify a limitation, articulate a design choice).

> "Quote 1"

> "Quote 2"

---

## Cross-References

### Complements entries in corpus
- `paper_a`: how this builds on / validates / extends that entry

### Contradicts / Tensions
- `paper_c`: what conflicts and how to interpret it

### Cross-corpus connections
- corpus X, entry `paper_d`: why this bridge matters

### Related entries to add
- HIGH / MEDIUM / LOW: ...

---

## Author Notes

### Priority justification
- Why is this source `CRITICAL` / `HIGH` / `MEDIUM` / `LOW` for this project?

### Use this source for
- query / use case 1–5

### Do NOT use this source for
- query type → better source / reason

### Curation notes
- terms needing harmonization, notation to flag, index sections to update, gaps exposed

---

## Related Concepts

List keywords and concepts that support retrieval and indexing.

---

## Quality Checklist

- [ ] precise terminology of the discipline is used throughout
- [ ] the source-type contextualization in Author Notes is complete
- [ ] assumptions are explicit
- [ ] novel contributions are distinguished from inherited components
- [ ] quantitative or qualitative results include the relevant specifics
- [ ] at least 5 useful direct quotes are included
- [ ] cross-references are present (including cross-corpus when relevant)
- [ ] the project-relevance relationship section is complete
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated
- [ ] the corpus `README.md` registry and counts have been updated
