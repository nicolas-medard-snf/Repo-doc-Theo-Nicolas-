---
name: lab-evolution-history
description: Document every significant modification to the agent system itself — agent definitions, skills, orchestration protocols, knowledge-structure changes. System-level traceability. Use after any change to how the system is built.
---

# Lab Evolution History (System History)

## Purpose

Record every significant modification to the **system itself** — the instrument, not the content. This is the chronological record of how the agent system evolved: agents added or changed, skills created or modified, orchestration rules updated, corpus structure restructured.

This is a traceability artifact, not optional documentation.

## Who triggers it

- `planning_timing_agent` (primary) — after system modifications
- the main orchestrating agent, when it modifies system infrastructure

## When triggered

After: agent-definition changes; skill creation/modification; orchestration-protocol updates; knowledge-structure restructuring; new operating modes; the addition or removal of a corpus.

## Procedure

1. Identify all system changes since the last logged entry.
2. Write a structured entry with the sections below.
3. Update `Doc/System_history/README.md` index (date + one-line summary + link).

## Entry Structure

```markdown
# YYYY-MM-DD — [Short Title]

## Context
What prompted this change.

## Changes (per component)
- **Agents**: [what changed]
- **Skills**: [what changed]
- **Orchestration**: [what changed]
- **Knowledge structure**: [what changed]

## Rationale
Why this change was made.

## Expected impact
What should now work better, and what to watch.

## Risks
What this change could break.

## Links
- related project-history entries
- affected files
```

## Output

`Doc/System_history/YYYY-MM-DD_short_title.md` — a logbook entry describing what changed, why, and the expected impact.

## Boundary

This skill tracks the **system** (the instrument). Content/decision evolution is tracked separately by the `project-history` skill (`Doc/Project_history/`). Keep the two distinct.
