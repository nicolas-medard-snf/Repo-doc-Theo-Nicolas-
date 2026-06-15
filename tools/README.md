# Tools — drop-in, level-agnostic utilities

This folder holds **standalone tools** you can add to a project at **any level**, independently of which seed you installed. They are not part of the level supersets — they are optional utilities that operate *on* the system rather than producing content.

Each tool here is self-describing: read its file, then copy it into the matching place in your project.

## Available tools

| Tool | File | Drop it into | What it does |
|------|------|--------------|--------------|
| System Integrity Guardian | `system_integrity_guardian.md` | `.cursor/Agents/` | An independent auditor that checks the system for orphan files, broken references, count mismatches, and missing traceability. It flags problems; it never fixes them. |

> The Integrity Guardian is also bundled inside Level 1 and Level 2 (where an orchestrator routes its findings). It is provided here as a standalone tool so a **Level 0** project — which has no orchestration layer — can still run a one-off health check.

## How to use a tool

1. Copy the tool's file into the indicated location in your project (e.g. `system_integrity_guardian.md` → `.cursor/Agents/`).
2. If the tool keeps memory, create an empty memory file under `.cursor/agents_memory/` with the matching name.
3. Invoke it on demand: ask for a "system integrity check" or "documentation audit".

## When to run the Integrity Guardian

- After adding new corpora, experts, or skills.
- Periodically during active work (for example, weekly).
- Before sharing or handing off the project, to confirm the knowledge system is internally consistent.

It is safe to run at any level and requires nothing beyond the files already in your project.
