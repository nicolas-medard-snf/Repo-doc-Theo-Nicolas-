# Ideation Reports

This folder holds the file-based handoffs of an **ideation cycle**. All ideation outputs are persisted here as files (not just chat), so every agent reads from files.

## File-based handoff per cycle

| Output | File | Written by |
|--------|------|------------|
| Expert landscape report | `cycle_{ID}_landscape_{corpus}.md` | each `expert_<corpus>` (via `corpus-driven-ideation`) |
| Path synthesis | `cycle_{ID}_path_synthesis.md` | `consultant_cross_domain` |
| Path enrichment | `cycle_{ID}_path_enrichment.md` | `skeptical_reviewer` |

`{ID}` is the cycle identifier (e.g. `001`). After enrichment, `experiment_tracker` logs the resulting items in `Doc/Hypotheses/idea_backlog.md`.

This folder starts empty; reports accumulate per cycle.
