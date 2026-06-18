# Memory — planning_timing_agent

Orchestrator / work prioritizer. See `.cursor/Agents/planning_timing_agent.md`.

> Store: per-corpus state snapshots; recurring budget-overrun patterns; recurring corpus tensions surfaced by enrichment; the deferred backlog.

## Per-corpus state snapshot (2026-06-18)
| Corpus | Entries | Last enrichment | Open gaps |
|--------|---------|-----------------|-----------|
| A_Genomic_Signal | 6 | none | A4 empty; A2/A3 OCR stubs |
| B_Therapeutic_Context | 1 | none | no B2/B4 primary entry |
| C_Cancer_Subtype | 0 | none | 0 entries (cross-ref only) |
| D_Clinical_Endpoint | 2 | none | no D1_pCR / D2 primary entry |
| E_Study_Type | 3 | none | E6 empty; OCR backlog (all 3) |

## Deferred backlog
- OCR of 5 non-text-extractable PDFs (then upgrade reference entries to decision).
- Create primary C entries and a D1_pCR entry.

## Log
### 2026-06-18 — Initial system setup
- Task: produced first SYSTEM STATE report; experts + memory shells instantiated; system-history logged.
- Heuristic learned: corpus seeding (12 entries) preceded agent instantiation; align ownership to existing entries.
- Gap flagged: ideation cycle deferred until ≥1 corpus is decision-rich enough to reason from (A qualifies; awaiting user trigger).
