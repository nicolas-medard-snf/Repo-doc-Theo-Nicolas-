---
name: pdf_annotation
description: Annotate PDFs with structured, color-coded highlights aligned with a paper-reading strategy. Use when an expert agent needs to deeply read a source and produce a semantically annotated PDF, or when the user requests annotation.
---

# PDF Semantic Annotator

## Purpose

Turn a flat PDF into a structured study artifact by applying color-coded highlights and short notes anchored in the project goals.

This skill produces a persistent record of how an expert read a source — what mattered, what was deep, what was surprising, and what was a gap.

## Annotation tier system

| Color | Tier | What gets highlighted |
|-------|------|------------------------|
| Red | `critical` | Core definitions, essential facts, key equations, primary results |
| Green | `deep` | Mechanisms, methodology, mathematical reasoning, architectural details |
| Yellow | `insight` | Novel ideas, surprising results, bridges to the project goals |
| Pink | `gap` | Limitations, open questions, assumptions the project context challenges |

## Who can use this skill

- any corpus expert (`expert_<corpus>`)
- the user directly

## When triggered

- when reading and annotating a new source for a corpus
- after `ingest_article` for decision-corpus sources (recommended)
- when the user asks to "annotate" or "highlight" a PDF

## Required references

Before annotating, read:

1. the PDF being annotated
2. the existing markdown summary in the destination corpus (if any)
3. the destination corpus `CROSS_REFERENCE_INDEX.md`
4. the destination corpus `README.md`
5. the relevant section of `Doc/Project_description/project_overview.md`

## Procedure

1. Read the PDF and its existing markdown summary (if any).
2. Identify key passages through four lenses:
   - **Mechanism / argument lens** — what is this source actually claiming?
   - **Foundation lens** — what does this source require to be true?
   - **Bridge lens** — where does this source connect to the project goals?
   - **Adversarial lens** — where is this source vulnerable?
3. Create an annotation JSON list with entries of the form:
   ```json
   {
     "page": 4,
     "tier": "deep",
     "text_excerpt": "...",
     "note": "short project-grounded note (<= 2 sentences)"
   }
   ```
4. Run `pdf_annotator.py` to apply highlights.
5. Report the annotation distribution (counts per tier) and any corpus gaps discovered.

## Output

- `<paper_id>_annotated.pdf` + `<paper_id>_annotations.json` co-located with the original PDF.

## Dependencies

- Python 3.10+
- PyMuPDF (`pip install PyMuPDF`)

## Tool location

- `.cursor/Skills/pdf_annotation/pdf_annotator.py`

## Notes

- Notes must be **short** (<= 2 sentences) and **project-grounded** (refer to the corpus scope or an anchor question).
- Aim for 15-40 annotations on a 10-20 page paper. More than that and the artifact stops being legible.
