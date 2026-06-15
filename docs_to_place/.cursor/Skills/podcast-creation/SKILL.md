---
name: podcast-creation
description: Turn one or more documents, notes, or corpus summaries into a spoken-audio explainer (podcast) for teaching and onboarding. Use when someone wants to *listen* to material — on a commute, for a seminar recap, or to onboard a teammate — rather than read it.
---

# Podcast / Audio Explainer Creation

This skill converts source documents into a listenable audio explainer using a simple, pluggable pipeline:

**Script transformation → prosody markup → text-to-speech → loudness normalization → audio file.**

Its purpose is **teaching and transmission**: making indexed knowledge easy to absorb by ear. It does not add new knowledge to a corpus.

## When to Use

- "Turn this into a podcast I can listen to on the way to work."
- "Make an audio explainer of this corpus / this paper / this design note."
- Onboarding material a new teammate can listen to before reading the full corpus.
- A spoken recap of a seminar, a decision, or a landscape analysis.

## Pipeline Overview

The pipeline has five stages. The first and last are mandatory; the TTS engine in the middle is **your choice** — any of a local neural TTS, a cloud TTS API, or the operating system's built-in speech command will work.

| Stage | What happens | Tooling (pick what you have) |
|-------|--------------|------------------------------|
| 1. Script transformation | Rewrite the source into spoken language: no markdown, no bullets, no headers read aloud | An LLM, or write it by hand |
| 2. Prosody markup | Insert pause markers and emphasis | Plain-text convention (below) |
| 3. Synthesis | Text → speech | Neural TTS (local/cloud) **or** OS `say`/`espeak` |
| 4. Normalization | Even out loudness to a broadcast level | `ffmpeg loudnorm` (≈ -16 LUFS) |
| 5. Export | Produce a portable file | MP3 (cross-platform) |

## Structure of the Explainer (always this order)

1. **Executive summary (first, ~2 min).** Synthesize everything so the listener can decide within two minutes whether to continue. Open with a one-sentence framing of what they are about to hear.
2. **Body.** One section per source document or major theme. Explain like a knowledgeable colleague, not a reader: include the "why it matters", the caveats, the take-home of each section.
3. **Conclusion (~1 min).** At most three takeaways, then a short sign-off.

## Step-by-Step Procedure

### Step 1 — Identify the sources

Read every document provided. Ground the explainer in the corpus index and `project_overview.md` so the framing is correct.

### Step 2 — Write the script

Save the script as plain text, e.g. `Doc/audio/podcast_YYYY-MM-DD_<short_title>.speech.txt`.

Formatting rules:

- Plain prose only — no markdown, no headers, no bullet characters.
- Insert prosody markers at logical boundaries:
  - `[pause_short]` — after a key sentence.
  - `[pause_long]` — between two ideas in a section.
  - `[section_break]` — between sections.
- Wrap critical terms, numbers, and results in `**double asterisks**` so the synthesis step can add emphasis.
- Write numbers as words.
- Write the executive summary last, then move it to the top.

Pacing: ~150 words/min. Target ~2000–2800 words for a 15–18 minute explainer.

### Step 3 — Synthesize the audio

Use whichever engine is available. Two reference options:

- **Neural TTS (preferred for quality):** feed the script to a local or cloud TTS engine, choosing a voice and the language of the script. Strip or interpret the prosody markers as the engine supports.
- **OS fallback (always available):** strip the prosody markers, then use the system speech command. Example:

```bash
sed 's/\[pause_short\]//g; s/\[pause_long\]//g; s/\[section_break\]//g; s/\*\*//g' \
  "Doc/audio/podcast_YYYY-MM-DD_<title>.speech.txt" > /tmp/clean.txt
# macOS:  say -f /tmp/clean.txt -o out.aiff
# Linux:  espeak -f /tmp/clean.txt -w out.wav
```

### Step 4 — Normalize and export

```bash
ffmpeg -i out.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 -b:a 192k podcast.mp3
```

### Step 5 — Verify and report

Report the output file, its estimated duration, and the executive-summary content so the listener knows what they are getting.

## Tone and Style

- Conversational, like a colleague explaining rather than reading.
- Natural spoken transitions ("What's interesting here…", "Concretely…", "So that's why…").
- Never say "dash", "bullet", or "slash" — rephrase into sentences.
- Never read headers, column names, or formatting characters.

## Dependencies

- `ffmpeg` for normalization (required).
- A TTS engine of your choice (neural TTS for quality, or the OS speech command as a zero-install fallback).
- Optionally an LLM for the script-transformation step; otherwise the script is written by hand.

## Do Not Do

- Do not read raw markdown aloud.
- Do not skip the executive summary — it is what makes the audio scannable.
- Do not invent content not present in the sources; this skill transmits knowledge, it does not create it.
