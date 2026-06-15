---
name: project-history
description: Record the content evolution of the project — how questions, decisions, directions, and major findings develop over time. Distinct from system history (which tracks the instrument). Use after any significant content decision or direction change.
---

# Project History (Content History)

## Purpose

Record the **content narrative** of the project — how its questions, decisions, directions, and major findings evolve. This is distinct from system history: it tracks the *what and why of the work*, not the *evolution of the tooling*.

## Who triggers it

- `planning_timing_agent` (primary) — after a significant content event
- the main orchestrating agent when acting as orchestrator

## When triggered

After: a major curation decision (e.g. growing a new corpus, deprioritizing one); a direction change; a significant finding surfaced by enrichment or cross-corpus analysis; a decision to pursue or abandon a line of inquiry. (At Level 2, also after ideation cycles, idea selection, proposal/review decisions.)

## Procedure

1. Identify the content event and its stage.
2. Write a structured entry with the sections below, preserving the reasoning (including rejected alternatives).
3. Update `Doc/Project_history/README.md` index (date + one-line summary + link).

## Entry Structure

```markdown
# YYYY-MM-DD — [Short Topic] (PH-NNN)

## Question / Trigger
What question or event this entry records.

## Context
The state of the project when this happened.

## What was decided / found
The substantive content.

## Reasoning
Why — including alternatives considered and rejected.

## Consequences
What this changes for the corpora or the project's direction.

## Links
- related system-history entries
- affected corpora / documents
```

## Output

`Doc/Project_history/YYYY-MM-DD_short_topic_PH-NNN.md` — a content-narrative entry with a unique ID and cross-links.

## Boundary

This skill tracks the **content** (the work). System/tooling evolution is tracked by `lab-evolution-history` (`Doc/System_history/`). Both must stay consistent; `system_integrity_guardian` verifies they do.
