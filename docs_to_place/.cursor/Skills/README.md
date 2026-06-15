# Skills Registry — Level 2 (Expert + Knowledge + Organization + Ideation)

Skills are **reusable procedural protocols** that agents invoke. They are **stateless** — state lives in agent memory files and corpus indices.

## Inventory (Level 2)

### Knowledge management (Level 0)

| Skill | Directory | What it does |
|-------|-----------|--------------|
| Article Ingestion | `ingest_article/` | Source → structured corpus entry + index update |
| Corpus Enrichment | `corpus-enrichment-analysis/` | Second-order layer over one corpus |
| Repository Ingestion | `repo-ingestion/` | Extract traceable knowledge from a code repository |
| Repository Cross-Comparison | `repo-cross-comparison-analysis/` | Compare how several codebases solve one design problem |
| Podcast / Audio Explainer | `podcast-creation/` | Turn corpus material into a spoken explainer for teaching |
| PDF Annotator | `pdf_annotation/` | Color-coded PDF highlights (+ tool) |
| MD Navigator | `md-navigator/` | Browsable HTML map (+ tool) |
| MD to PDF | `md-to-pdf/` | Markdown → print-ready PDF (+ tool) |
| Cross-Corpus Enrichment | `cross-corpus-enrichment-analysis/` | Bridge two corpora — owned by `consultant_cross_domain`, **not** experts |

### Organization (Level 1)

| Skill | Directory | What it does |
|-------|-----------|--------------|
| Lab Evolution History | `lab-evolution-history/` | Log changes to the system itself → `Doc/System_history/` |
| Project History | `project-history/` | Log content evolution → `Doc/Project_history/` |

### Ideation (added at Level 2)

| Skill | Directory | What it does | Owner |
|-------|-----------|--------------|-------|
| Corpus-Driven Ideation | `corpus-driven-ideation/` | Produce a corpus landscape report for an ideation cycle | corpus experts |
| Candidate Idea Register | `candidate-idea-register/` | Log a newly discovered method as a candidate without reopening decisions | corpus experts |

## Skill vs Agent Boundary

| Concern | Where it lives |
|---------|----------------|
| Who am I? What do I own? | Agent definition |
| How do I execute this task? | Skill |
| What workflow do I follow? | `orchestration_guideline.md` |
| What did I do last session? | Agent memory |

## Notes

- The ideation engine is mostly **agent protocol** (orchestration Mode 4), with `corpus-driven-ideation` as the per-expert procedure. Path synthesis and enrichment formats live in the `consultant_cross_domain` and `skeptical_reviewer` agent definitions.
- Tool dependencies: `pdf_annotation` needs PyMuPDF; `md-to-pdf` needs pandoc + xelatex.
