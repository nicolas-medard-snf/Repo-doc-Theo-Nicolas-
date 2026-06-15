# How to Add Sources to the Corpora

**Purpose**: step-by-step guide for adding any curated source (paper, book, essay, technical report, transcribed text) to any corpus under `Doc/Corpus/`.

The goal is **not** to create passive summaries. The goal is to create **indexed knowledge** that expert agents can reason through reliably.

Before using this guide, also read:

- `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`
- `Doc/Project_description/project_overview.md`
- the destination corpus `README.md`
- the destination corpus `CROSS_REFERENCE_INDEX.md`

---

## Quick workflow

```
1. Add source (PDF, EPUB, transcribed text)
2. Choose destination corpus and category
3. Rename the source to the canonical filename and move it into the final category folder
4. Create the markdown summary from PAPER_TEMPLATE_GENERAL.md
5. Apply the 6 critical improvements
6. Update CROSS_REFERENCE_INDEX.md (mandatory)
7. Update the corpus README.md (registry + category counts) (mandatory)
8. Verify retrieval and project relevance (mandatory)
```

**Estimated time per source**: decision sources (deep ingestion) 15–25 min with AI assistance; reference sources (template ingestion) 5–10 min.

---

## Step 1 — Add the source

### 1.1 Filename convention

Use `firstauthor_year_short_keyword.pdf`. Avoid uppercase, spaces, missing year or keyword.

### 1.2 Place the source in the right corpus area

If no category exists yet, create a clear category folder rather than dropping the file at the corpus root. The source must not remain in a staging folder once ingested — rename it and move it into the same final category directory as the markdown summary.

---

## Step 2 — Choose the target corpus

Choose based on the source's main value for the project, not on its surface topic. See `Doc/Project_description/project_overview.md` for boundary rules. If a source spans multiple corpora, place it where it is most useful as a **reasoning object** and cross-reference it from the relevant indices.

---

## Step 3 — Create the markdown summary

Use `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

### Required bridge to the project

Every entry must include `Relationship with the project's goals`. It must name which corpus scope the source maps to (and any bridge corpus), name the anchor question(s) it engages with, and state whether the source is directly reusable, indirectly inspiring, or background.

---

## Step 4 — Fill the metadata carefully

### Relevance score guidance
- **5** critical, referenced repeatedly · **4** highly useful for a major sub-area · **3** useful background · **2** tangential · **1** fills a very specific gap only

### Priority level guidance
- **CRITICAL** foundational/repeatedly needed · **HIGH** important and likely to recur · **MEDIUM** useful but not central · **LOW** niche/background

### `corpus_role`
- **`decision`**: source you would actively build from, reuse, cite as primary support, or test against. Feeds the `corpus-driven-ideation` skill (if installed).
- **`reference`**: review, survey, foundation, tangential method, or background.

### `temporal_status`
- **`active_candidate`**: current work or older work still standard on its topic
- **`historical_pedagogical`**: important historically but superseded by newer work in the corpus

---

## Step 4b — Deep ingestion for decision sources

Decision sources require a higher standard because they directly feed ideation and synthesis.

1. Decision sources MUST be ingested by reading the actual document, not abstracts or third-party summaries.
2. Read the file co-located with the `.md` summary.
3. All `[TO BE COMPLETED]` markers must be filled — no placeholder text in a decision entry.
4. Quotes must come from the body.
5. For empirical sources: extract method details, sample sizes, and effect sizes from the body.
6. For formal sources: the central argument or proof structure must be transcribed faithfully.

---

## Step 5 — Apply the 6 critical improvements

1. **Precise terminology** — state precisely what the source claims, with the discipline's actual vocabulary, named operations, equations, or rhetorical structures.
2. **Explicit assumptions** — state what the source assumes about its evidence base, framework, scope, and context.
3. **Source-type contextualization** — in `Author Notes`, specify what type of source it is, what it is good for, what it is not good for, and who should retrieve it.
4. **Quantitative or qualitative specifics** — extract effect sizes/tables (empirical) or precise claim scope and canonical examples (non-empirical).
5. **Direct quotes** — 5–10 short body quotes that ground a mechanism, claim, or limitation. No filler.
6. **Cross-references** — identify what this complements, what it conflicts with, and what entries it reveals should be added.

---

## Step 6 — Update `CROSS_REFERENCE_INDEX.md`

After adding a source, update the destination index under at least one of: concepts; methods / mechanisms / schools of thought; open questions / problems; contradictions / tensions; hub entries; unexplored combinations.

---

## Step 7 — Update the corpus `README.md`

The corpus README is the **authoritative registry**. If a source is ingested but not listed, it is invisible to agents scanning the corpus.

1. **Category table**: increment the count for the relevant category row
2. **Total count**: update the total
3. **Full Registry**: add the new `paper_id` and a short one-line description under the correct category

When batch-ingesting, update the README once at the end of the batch.

---

## Step 8 — Verify project relevance

- [ ] entry follows `PAPER_TEMPLATE_GENERAL.md`
- [ ] metadata is complete enough for retrieval
- [ ] the project-relevance section is filled
- [ ] the 6 improvements are present
- [ ] the source is in the correct corpus and category
- [ ] the source has been renamed and co-located with the `.md`
- [ ] `CROSS_REFERENCE_INDEX.md` was updated
- [ ] the corpus `README.md` registry and counts were updated
- [ ] the summary is useful for this project, not just generally informative

---

## Step 9 — Retrieval check

- Can the source be found by `paper_id`?
- Can it be found through the relevant concept or method section in the index?
- Does the project-relevance section make its use clear?

If no, improve the entry or index before moving on.

---

## Common pitfalls

**Do not**: write generic summaries with no project bridge; omit assumptions; omit specifics; omit cross-references; treat the source as standalone; use raw PDFs as the normal long-term reasoning interface.

**Do**: write for future use by the expert agents; be explicit about fit with the project; update the index and README immediately; report gaps and contradictions honestly; prefer precise, reusable content.

---

## Final rule

A source is not "ingested" until: the markdown summary is structured; the source has been renamed and co-located with the summary; the project bridge is explicit; `CROSS_REFERENCE_INDEX.md` is updated; the `README.md` registry is updated (entry + counts); the source becomes usable by the expert agents.
