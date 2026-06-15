---
name: md-navigator
description: Generate a browsable HTML navigator over a markdown subtree (e.g. one corpus, or the whole Doc/Corpus). Useful for a quick visual map of curated knowledge.
---

# MD Navigator

## Purpose

Generate an interactive HTML file that maps a markdown subtree of the project. Useful when the user wants to scan a corpus visually, audit the structure, or share a snapshot.

## Who can use this skill

- the user
- any agent who needs to inspect a corpus structurally

## Usage

```bash
python3 .cursor/Skills/md-navigator/generate_navigator.py \
  --root Doc/Corpus/<your_corpus> \
  --output navigator.html
```

## Inputs

- `--root` : path to the markdown subtree to scan
- `--output` : output HTML path

## Output

- one self-contained HTML file at the chosen output path

## Notes

- The script reads markdown headings and front-matter to build the tree.
- Generated HTML can be opened directly in a browser; no server needed.
- Regenerate on demand; do not commit the HTML.
