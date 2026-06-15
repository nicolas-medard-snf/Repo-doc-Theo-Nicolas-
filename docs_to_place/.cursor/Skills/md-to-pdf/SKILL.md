---
name: md-to-pdf
description: Convert markdown files to clean, print-ready PDFs using pandoc + xelatex. Markdown syntax (##, **, `, etc.) is rendered invisibly — output looks like a proper document.
---

# MD to PDF

## Purpose

Convert markdown files in this repository to clean, print-ready PDFs. Useful for offline reading, printing, or sharing.

## Quick usage

```bash
# Single file
bash .cursor/Skills/md-to-pdf/convert.sh Doc/Corpus/<your_corpus>/some_entry.md

# Whole directory
bash .cursor/Skills/md-to-pdf/convert.sh Doc/Corpus/<your_corpus>/

# Directory -> custom output folder
bash .cursor/Skills/md-to-pdf/convert.sh Doc/Corpus/<your_corpus>/ --outdir ~/Desktop/PDFs_to_print
```

## Dependencies

- pandoc
- xelatex (or pdflatex)

## Settings

- Georgia 12pt, 2.5 cm margins, 1.4 line spacing, xelatex engine (handles non-ASCII characters).

## Output

- `<file>.pdf` co-located with the source, or in `--outdir` if specified.
