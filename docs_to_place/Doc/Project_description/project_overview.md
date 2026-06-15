# Project Overview

> **This is a template you fill once, at install time.** It is the shared context layer every expert agent reads before reasoning. Keep it small but precise. Replace every `<...>` placeholder and delete this quote block when done.

---

## 1. What this project is

`<One paragraph: what the project is about, what it is trying to produce or understand, and over what time horizon.>`

## 2. Goals and anchor questions

The project is organized around a small set of **anchor questions** — the questions the knowledge system exists to help answer.

- **AQ-1**: `<anchor question>`
- **AQ-2**: `<anchor question>`
- **AQ-3**: `<anchor question>`

Every corpus entry's `Relationship with the project's goals` section should connect back to at least one anchor question.

## 3. Corpora

List the corpora this project curates. Each becomes a directory under `Doc/Corpus/` and gets one expert agent (`.cursor/Agents/expert_<short_name>.md`).

| Short name | Corpus directory | Scope (one line) |
|------------|------------------|------------------|
| `<short_1>` | `Doc/Corpus/<dir_1>/` | `<scope>` |
| `<short_2>` | `Doc/Corpus/<dir_2>/` | `<scope>` |
| `<short_3>` | `Doc/Corpus/<dir_3>/` | `<scope>` |

## 4. How the corpora relate (bridges)

Describe the most important relationships between corpora — which corpus supplies upstream ideas for which other corpus. These bridges drive the `cross-corpus-enrichment-analysis` skill.

- `<corpus A>` → `<corpus B>`: `<why this bridge matters>`
- `<corpus C>` → `<corpus A>`: `<why this bridge matters>`

## 5. Boundaries

State explicitly what is **out of scope** so agents do not drift:

- `<topic intentionally excluded>`
- `<topic intentionally excluded>`

## 6. Priority

If one corpus should be grown first, say which and why:

- **Priority corpus**: `<short_name>` — `<reason>`
