# Agents — Level 2 (Expert + Knowledge + Organization + Ideation)

This folder holds the **agent definitions** for the knowledge system. An agent definition declares an agent's identity, what it owns, how it reasons, and its boundaries.

## What is in Level 2

| File | Layer | Role |
|------|-------|------|
| `expert_corpus_template.md` | Expert | Generic, copyable corpus-owning expert (also produces landscape reports) |
| `orchestration_guideline.md` | Organization | Authoritative routing protocol — includes the ideation pipeline (Mode 4) |
| `planning_timing_agent.md` | Organization | Orchestrator: routes work, prioritizes, triggers history, runs ideation cycles |
| `system_integrity_guardian.md` | Organization | Independent auditor of consistency and traceability |
| `consultant_cross_domain.md` | Ideation | Cross-corpus synthesis + assembles landscape reports into research paths |
| `model_creator.md` | Ideation | Proposal author: turns paths/questions into structured proposals |
| `skeptical_reviewer.md` | Ideation | Destruction-tests proposals; enriches ideation paths |
| `experiment_tracker.md` | Ideation | Tracks the idea/proposal STATE lifecycle (idea backlog) |

## Design philosophy

A **team of scientific experts with structured knowledge, an organizational layer, and an ideation engine**:

1. **Corpus ownership** + **index-first reasoning**.
2. **Single orchestrator** (`planning_timing_agent`) + **independent audit** (`system_integrity_guardian`).
3. **Protocol-driven ideation**: experts → landscape reports; consultant → paths; reviewer → enrichment; creator → proposals; tracker → state.
4. **Traceability + memory** everywhere.

## How to instantiate

- **Experts**: copy `expert_corpus_template.md` once per corpus to `expert_<short_name>.md`, fill placeholders, create a memory shell, create the corpus skeleton.
- **Single-instance agents** (`planning_timing_agent`, `system_integrity_guardian`, `consultant_cross_domain`, `model_creator`, `skeptical_reviewer`, `experiment_tracker`): no copying — just create their memory files.

## The ideation cycle in one line

`experts (landscape) → consultant (paths) → reviewer (enrichment) → user picks a path → model_creator (proposals) → reviewer (review loop) → tracker (state) → planner (history)`. Full protocol: `orchestration_guideline.md` Mode 4.
