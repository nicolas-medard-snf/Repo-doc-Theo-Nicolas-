# Agent Memory

Each agent keeps a persistent memory file here: `.cursor/agents_memory/<agent_name>_memory.md`.

Memory provides **session continuity** — what an agent learned, decided, or flagged in past sessions — so it does not start cold each time.

## Convention

When an instantiated expert completes a substantive task, append an entry:

```text
### YYYY-MM-DD — [Task Description]

- **Task**: [what was done]
- **Key output**: [file path or summary]
- **Heuristic learned**: [any reusable pattern or constraint discovered]
- **Gap flagged**: [any missing knowledge or corpus gap identified]
```

## Files

Create one memory file per instantiated expert: `expert_<short_name>_memory.md`. This folder starts empty except for this README; the bootstrap/integration prompt creates the per-expert memory shells.
