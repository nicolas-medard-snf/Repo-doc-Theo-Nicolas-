# Orchestration Guideline — Level 2 (Expert + Knowledge + Organization + Ideation)

This file defines how the agents collaborate. It is an operating protocol, not background prose. It is the **single authoritative source** for routing logic, agent interaction maps, and collaboration rules.

For agent role details → read the individual agent files in `.cursor/Agents/`.
For knowledge system details → read `Doc/Project_description/knowledge_system_specification.md`.

## Design Philosophy

The system behaves like a **team of scientific experts with structured knowledge, an organizational layer, and an ideation engine** — not a set of generic LLM utilities.

1. **Corpus ownership** — experts own domains of knowledge.
2. **Index-first reasoning** — agents reason through `CROSS_REFERENCE_INDEX.md`, not raw dumps.
3. **Explicit role boundaries** — each agent has clear responsibilities and non-responsibilities.
4. **Protocol-driven collaboration** — multi-agent work follows explicit loops, not ad hoc handoffs.
5. **Single orchestrator** — `planning_timing_agent` routes and sequences all multi-step work.
6. **Independent audit** — `system_integrity_guardian` keeps the system consistent.
7. **Traceability + memory** — every change is logged (system vs content history); every agent keeps memory.

## System Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                      ORGANIZATIONAL LAYER                        │
│   ┌─────────────────────────┐   ┌────────────────────────────┐  │
│   │  planning_timing_agent  │◄─►│  system_integrity_guardian │  │
│   └───────────┬─────────────┘   └────────────────────────────┘  │
├───────────────┼──────────────────────────────────────────────────┤
│               │            EXPERT LAYER (corpus owners)           │
│   ┌───────────▼───────┐  ┌──────────────────┐  ┌──────────┐      │
│   │  expert_<corpus1> │  │ expert_<corpus2> │  │  ...     │      │
│   └─────────┬─────────┘  └────────┬─────────┘  └────┬─────┘      │
│             └───────────┬─────────┘─────────────────┘            │
│                         ▼                                        │
│             ┌───────────────────────┐                           │
│             │ consultant_cross_domain│  synthesizes / bridges    │
│             └───────────┬───────────┘                           │
├─────────────────────────┼────────────────────────────────────────┤
│                         │   CREATION & CRITIQUE LAYER             │
│             ┌───────────▼──────────┐   ┌────────────────────┐    │
│             │    model_creator     │◄─►│  skeptical_reviewer │    │
│             └───────────┬──────────┘   └────────────────────┘    │
├─────────────────────────┼────────────────────────────────────────┤
│                         │   PERSISTENCE LAYER                     │
│             ┌───────────▼──────────┐                             │
│             │  experiment_tracker  │  idea/state lifecycle        │
│             └──────────────────────┘                             │
└────────────────────────────────────────────────────────────────┘
```

## Roles

| Agent | Function | Writes | Must not write |
|-------|----------|--------|----------------|
| `expert_<corpus>` | owns and curates one corpus; produces landscape reports | entries, indices, enrichment, landscape reports | another corpus's content, code |
| `consultant_cross_domain` | synthesizes across corpora; assembles paths | bridge docs, path synthesis | raw corpus content, verdicts, code |
| `model_creator` | invents proposals | proposals, revision responses | reviews, corpus content, code |
| `skeptical_reviewer` | destruction-tests; enriches paths | reviews, path enrichment | proposals, corpus content, code |
| `experiment_tracker` | tracks idea/proposal STATE | backlog state, lifecycle records | proposals, critique, content |
| `planning_timing_agent` | routes work, prioritizes, triggers history | routing, plans, state summaries | domain verdicts without expert input |
| `system_integrity_guardian` | audits consistency + traceability | integrity reports | content, orchestration, history entries |

## Agent ↔ Corpus Ownership

Each corpus under `Doc/Corpus/` is owned by exactly one `expert_<short_name>.md`, recorded in `Doc/Project_description/project_overview.md`.

## Operating Modes

### Mode 1 — Curation (default loop)

`planning_timing_agent` → `expert_<corpus>` (runs a KM skill, updates index/README) → `planning_timing_agent` triggers history → agents update memory.

### Mode 2 — Cross-corpus bridge

`planning_timing_agent` routes a two-corpus dependency to `consultant_cross_domain`, which runs `cross-corpus-enrichment-analysis`.

### Mode 3 — Integrity audit

`system_integrity_guardian` produces an INTEGRITY REPORT; `planning_timing_agent` routes corrections (the guardian never fixes anything itself).

### Mode 4 — Scientific Ideation (the headline Level 2 capability)

Use when the project needs to generate testable questions from corpus knowledge and organize them into coherent research paths. Experts act as **landscape analysts**; the consultant assembles **paths**; the reviewer **enriches** them.

```
USER / planning_timing_agent
   │ 1. Triggers ideation (scope, cycle ID)
   ├──────────────┬──────────────┐
   ▼              ▼              ▼
 expert_<c1>   expert_<c2>   expert_<c3>
   │ reads its corpus + project_overview
   │ 2. Produces CORPUS LANDSCAPE REPORT
   │    (mandatory foundations, open choices, idea chains, surprises, gaps)
   │ 3. Saves to Doc/Hypotheses/ideation_reports/cycle_{ID}_landscape_{corpus}.md
   └──────────────┬──────────────┘
                  ▼
       consultant_cross_domain
                  │ 4. Reads all landscape reports
                  │    Merges mandatory foundations → shared infrastructure
                  │    Assembles 2-3 complete research PATHS from decision points
                  │ 5. Saves cycle_{ID}_path_synthesis.md
                  ▼
         skeptical_reviewer
                  │ 6. Enriches each step/path (feasibility, risk, decision rules)
                  │    Compares paths head-to-head + argued recommendation
                  │ 7. Saves cycle_{ID}_path_enrichment.md
                  ▼
              USER
                  │ 8. Selects a path (or hybrid); confirms shared infrastructure
                  ▼
       experiment_tracker → updates idea_backlog.md (selected/deferred states)
                  ▼
       planning_timing_agent → logs project-history; routes selected path
                  ▼
       model_creator → develops detailed proposals for the selected path
                  │ → skeptical_reviewer full review → revision loop → tracker records
```

All ideation outputs are **persisted as files**; agents read from files, not chat.

### Mode 5 — Proposal Validation

`model_creator` writes a full proposal → targeted expert advisories (+ consultant if they conflict) → revision → `skeptical_reviewer` full review (approve / approve-with-caveats / revise / reject) → `model_creator` REVISION RESPONSE → repeat (max ~2 cycles) → `experiment_tracker` records the transition → `planning_timing_agent` logs history.

### Mode 6 — Vigilance

After ingestion/enrichment, the owning expert may run the `candidate-idea-register` skill to log a new method as a candidate in `Doc/Hypotheses/candidate_ideas.md`, to be evaluated at a defined decision point — **without reopening settled decisions**.

## File-Based Handoff Rules (ideation)

| Output | File | Written by |
|--------|------|------------|
| Landscape report | `Doc/Hypotheses/ideation_reports/cycle_{ID}_landscape_{corpus}.md` | each expert |
| Path synthesis | `Doc/Hypotheses/ideation_reports/cycle_{ID}_path_synthesis.md` | `consultant_cross_domain` |
| Path enrichment | `Doc/Hypotheses/ideation_reports/cycle_{ID}_path_enrichment.md` | `skeptical_reviewer` |
| Proposal | `Doc/Hypotheses/proposals/YYYY-MM-DD_concept.md` | `model_creator` |
| Backlog state | `Doc/Hypotheses/idea_backlog.md` | `experiment_tracker` |

## Traceability Architecture

| Layer | Purpose | Location | Owner |
|-------|---------|----------|-------|
| System history | Evolution of the agent system | `Doc/System_history/` | `planning_timing_agent` via `lab-evolution-history` |
| Project history | Content/decision narrative | `Doc/Project_history/` | `planning_timing_agent` via `project-history` |
| State tracking | Current status of ideas/paths/proposals | `Doc/Hypotheses/idea_backlog.md` | `experiment_tracker` |
| Agent memory | Per-agent continuity | `.cursor/agents_memory/` | each agent |
| Integrity audit | Verifies all layers agree | on-demand reports | `system_integrity_guardian` |

## Review Authority

`skeptical_reviewer` has binding authority on proposal rigor status: `approve` / `approve-with-caveats` / `revise` / `reject`. It must not invent alternatives; it judges the artifact in front of it.

## Non-Bypass Rules

1. `model_creator` does not replace the experts.
2. `consultant_cross_domain` does not do primary corpus reading when an expert should.
3. `skeptical_reviewer` does not author proposals.
4. `experiment_tracker` does not reinterpret evidence on its own.
5. `planning_timing_agent` is the entry point for any multi-step task.
6. No agent skips its memory update after a substantive task.
7. No system change goes unlogged in `Doc/System_history/`; no significant content decision goes unlogged in `Doc/Project_history/`.
8. `system_integrity_guardian` only audits and flags — it never produces content, orchestrates, or fixes.
9. Experts never bypass `CROSS_REFERENCE_INDEX.md` when it exists.

## Message Formats

### Expert Request / Advisory

```text
--- EXPERT REQUEST
Question: [specific question]
Objective: [what decision depends on it]
Scope: [corpus / context to consult]
Output Needed: [expected structured output]
---
--- EXPERT ADVISORY
Question: [original]
Corpus Used: [index + files consulted]
Key Findings: 1... 2...
Risks / Gaps: ...
Recommendation: ...
Next Agent: [agent] -> [what it should do]
---
```

### Memory Update (every agent, after a task)

```text
### YYYY-MM-DD — [task]
- Task / Key output / Heuristic learned / Gap flagged
```
