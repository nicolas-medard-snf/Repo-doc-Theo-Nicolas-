---
name: candidate-idea-register
description: Vigilance procedure for newly discovered methods. After ingestion or enrichment, evaluate a new source against the active research direction and, if relevant, add a structured candidate entry to Doc/Hypotheses/candidate_ideas.md without reopening closed decisions.
---

# Candidate Idea Register

## Purpose

Keep the project scientifically vigilant **without thrashing**. When a newly ingested source proposes a method, framing, or result that could affect a planned direction, this skill captures it as a structured **candidate** — flagged for later evaluation at a defined decision point — rather than immediately reopening a settled plan.

This is the bridge between continuous curation (Level 0–1) and the structured ideation backlog (Level 2).

## When to Use

Trigger after `ingest_article` (or an enrichment pass) when the source is:

- a direct alternative to a planned approach
- a new state-of-the-art result on a relevant problem
- a new strategy for a known difficulty
- an efficiency improvement
- a reframing that affects an anchor question

## Priority Rubric

| Priority | Condition |
|----------|-----------|
| HIGH | Directly replaces or extends a planned step; clearly stronger than the current choice |
| MEDIUM | An additional comparator worth including in a planned evaluation |
| LOW | Interesting for future cycles; not immediately actionable |

## Procedure

1. **Check for duplicates** in `Doc/Hypotheses/candidate_ideas.md` and `Doc/Hypotheses/idea_backlog.md`.
2. **Confirm project relevance** via the anchor questions in `Doc/Project_description/project_overview.md`. If it does not engage an anchor question, do not add it.
3. **Identify the project hook** — which planned step, open choice, or anchor question this candidate touches.
4. **Assess priority** (HIGH / MEDIUM / LOW).
5. **Identify the decision point** — when this candidate should be evaluated (e.g. "next ideation cycle", "before selecting the fusion approach").
6. **Write the candidate entry** (template below).
7. **Update the Review History** table at the top of `candidate_ideas.md`.
8. **Notify `planning_timing_agent`** for HIGH-priority candidates only.
9. **Report** candidate ID, project hook, priority, decision point, and next action.

## Candidate Entry Template

```markdown
### CAND-NNN — [short title]
- **Source**: [paper_id]
- **Project hook**: [planned step / open choice / anchor question]
- **Priority**: HIGH | MEDIUM | LOW
- **Decision point**: [when to evaluate]
- **Trigger condition**: [what would promote this to the backlog]
- **Status**: watch | evaluate | implement | deferred | rejected
- **Linked action**: [what to do at the decision point]
```

## Status Lifecycle

`watch → evaluate → implement` (promoted to `idea_backlog.md`), or `deferred`, or `rejected` (always logged with rationale).

## Output

Updated `Doc/Hypotheses/candidate_ideas.md` + (for HIGH priority) a note to `planning_timing_agent`.

## Rule

This skill **does not reopen closed decisions**. It records vigilance so the project can revisit a choice at the right moment, deliberately, instead of reactively.
