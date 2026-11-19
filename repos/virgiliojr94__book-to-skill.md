# virgiliojr94/book-to-skill

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/virgiliojr94/book-to-skill)

> Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Turn books into agent skills |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 38.5k |
| 🍴 **Forks** | 4.1k |
| 🐞 **Open issues + PRs** | [37](https://github.com/virgiliojr94/book-to-skill/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-agents` `context-engineering` `document-processing` `edtech` `knowledge-base` `knowledge-management` `llm` `pdf-to-markdown` `rag` `self-study` `study-tools` `book-to-skill` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-05-01 |
| 📦 **Latest release** | [v2.0.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.0) — 2026-11-19 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 2.7 MB |

## 📦 Recent releases

### [v2.0.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.0)
<sub>2026-11-19 · today</sub>

> **[2.0.0] - 2026-11-19**
> **Added**
> - Replace the ASCII banner with two quiet lines, and fund the project at the end (#153)
> - Optional GitHub publishing for generated skills (#102)
> - Improve Persian chapter detection (#139)
> - Detect Hindi (Devanagari) chapter headings (#186)
> …

### [v1.4.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v1.4.0)
<sub>2026-08-10 · 3mo ago</sub>

> Extraction reliability release: six fixes for silent content loss or silent wrong answers, plus the first changelog generated from commit messages.
> **Highlights**
> - **Scanned PDFs fail fast.** An image-only PDF used to run the whole extraction chain — Docling across every page in technical mode — before failing with a message about Unicode sanitization. It now stops on the first pages in ~0.01s and tells you to run `ocrmypdf` (#130), and the docs finally state the limit (#132).
> - **Real words stopped being deleted.** Page-edge cleanup treated any short word built from `ivxlcdm` as a page number, so "MIX", "CIVIL" and "VIVID" vanished when they were alone on a page's first or last line (#119).
> - **Table-of-contents detection no longer depends on input order.** With multiple sources, `has_toc` was re-derived over the joined corpus and its 30k-char window only ever covered the first book — the same two books in the opposite order gave opposite answers (#114).
> - **A single unreadable file no longer aborts the batch** (#120), and `~` in a quoted glob is expanded, so the README's own example works (#118).
> …

### [v1.3.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v1.3.0)
<sub>2026-07-30 · 3mo ago</sub>

> **book-to-skill v1.3.0**
> 36 commits since v1.2.0. This release is security-heavy and adds multilingual chapter detection.
> **🔒 Security**
> - **Generated-skill prompt-injection scan** — a dependency-free advisory scanner flags instruction-override phrases, model-control tags, invisible Unicode, authority-widening frontmatter, and exfiltration-shaped content before a generated skill is accepted or published. Findings never echo attacker-controlled text (#73, #74).
> - **Invisible-Unicode extraction hardening** — every parser result now strips zero-width `U+200B/200C/200D/2060/FEFF` and the Unicode tag block `U+E0000–E007F`, reports the removal count, and rejects sources with no visible content after the scrub (#73, #75, #85).
> - **DOCX XXE / Billion Laughs** and **subprocess argument-injection** hardening, plus **dependency CVE review** on PRs (#53, #54).
> …

### [v1.2.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v1.2.0) — v1.2.0 — installable package + multilingual chapter detection
<sub>2026-06-17 · 5mo ago</sub>

> book-to-skill v1.2.0 turns the project into an installable Python package and makes chapter detection genuinely multilingual.
> **Highlights**
> **📦 Installable package + CLI**
> `book-to-skill` is now a real `book_to_skill` package: `pip install` it, run the `book-to-skill` console script or `python -m book_to_skill`, and pull only the extractors you need via extras (`epub`, `pdf`, `docx`, `rtf`, `technical`, `all`). The base install stays dependency-free with stdlib fallbacks, and `python3 scripts/extract.py` still works unchanged, so existing skill flows keep running.
> **🌍 Multilingual chapter detection**
> - Markdown / AsciiDoc ATX headings (`#`, `==`) detected when no numeric "Chapter N" is present.
> …

### [v1.1.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v1.1.0)
<sub>2026-06-12 · 5mo ago</sub>

> **[1.1.0] — 2026-06-12**
> **Added**
> - **GitHub Copilot CLI as a first-class target** — the same `SKILL.md` now
>   discovers, installs, and runs across GitHub Copilot CLI, Amp, and Claude Code
>   via the open Agent Skills standard. Skill Locations cover 8 discovery paths and
>   the script probe walks all of them (#30).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [feat(skill): add opt-in guided MCP setup directly in Step 0](https://github.com/virgiliojr94/book-to-skill/commit/a0fcb8cd004b017d07acf066510276311211d6a7) | virgiliojr94 |
| 2026-11-19 | [fix(skill): clarify Search & Read onboarding UX and bare-search handling](https://github.com/virgiliojr94/book-to-skill/commit/dad950d33e91e8f29d32d3f8053c42123892dc25) | virgiliojr94 |
| 2026-11-19 | [chore(release): v2.0.0](https://github.com/virgiliojr94/book-to-skill/commit/185936caf5781525d14c3deb08174f6d4feae4e4) | virgiliojr94 |
| 2026-11-19 | [docs(plan): record Profile A selection for TR-LEG in v2 ledger](https://github.com/virgiliojr94/book-to-skill/commit/e5b981dc32bb63450ffbce8b5c95e861b00697bd) | virgiliojr94 |
| 2026-11-19 | [docs(plan): record PR 4b and PR 5 completion in v2 ledger](https://github.com/virgiliojr94/book-to-skill/commit/2fe5c5d20ea49f6deaa6ec89eb0c3d86b426d5b6) | virgiliojr94 |
| 2026-11-19 | [docs(remote): document Search & Read mode, architecture, and MCP secu…](https://github.com/virgiliojr94/book-to-skill/commit/5ab8f5614494986ca2c04532f1aa4af8c5e359e6) | virgiliojr94 |
| 2026-11-19 | [test(remote): add offline mock MCP simulator, E2E flows, and security…](https://github.com/virgiliojr94/book-to-skill/commit/cdd50445c3f68b0d0ea88a3e8fab5e64abd51e4b) | virgiliojr94 |
| 2026-11-19 | [feat(skill): wire incremental remote generation and provenance specs](https://github.com/virgiliojr94/book-to-skill/commit/928189080754f8ebf5ada85e76dc017e9145084b) | virgiliojr94 |
| 2026-11-19 | [docs(plan): record PR 3 and PR 4a completion in v2 ledger](https://github.com/virgiliojr94/book-to-skill/commit/500f82a9fbd5f42c38e2eea681717ff9615204a4) | virgiliojr94 |
| 2026-11-19 | [feat(remote): add coverage reporting and prose-free provenance metadata](https://github.com/virgiliojr94/book-to-skill/commit/efe9025eee19a61cda6d0e15a659f852bdd1b413) | virgiliojr94 |

[See all commits ↗](https://github.com/virgiliojr94/book-to-skill/commits)

## ⬇️ Get it

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git
```
