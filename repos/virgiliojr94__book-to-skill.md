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
| ⭐ **Stars** | 38.9k |
| 🍴 **Forks** | 4.2k |
| 🐞 **Open issues + PRs** | [29](https://github.com/virgiliojr94/book-to-skill/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-agents` `context-engineering` `document-processing` `edtech` `knowledge-base` `knowledge-management` `llm` `pdf-to-markdown` `rag` `self-study` `study-tools` `book-to-skill` |
| 🕒 **Last activity** | 2026-11-22 (yesterday) |
| 📅 **Created** | 2026-05-01 |
| 📦 **Latest release** | [v2.0.1](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.1) — 2026-11-19 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 2.8 MB |

## 📦 Recent releases

### [v2.0.1](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.1)
<sub>2026-11-19 · 4d ago</sub>

> **[2.0.1] - 2026-11-19**
> **Added**
> - Add opt-in guided MCP setup directly in Step 0
> - Detect Arabic (الفصل/الباب) chapter headings (#346)
> - Detect Georgian (თავი) chapter headings (#325)
> **Documentation**
> …

### [v2.0.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.0)
<sub>2026-11-19 · 5d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [chore(release): v2.0.1](https://github.com/virgiliojr94/book-to-skill/commit/57f3db51ff338edfd940a255b885c60ac90e40fa) | virgiliojr94 |
| 2026-11-19 | [sec: resolve remaining high CodeQL test alerts and annotate empty exc…](https://github.com/virgiliojr94/book-to-skill/commit/c57deb8ce61d905d523b395e7d9f0071eef17d6c) | virgiliojr94 |
| 2026-11-19 | [chore(remote): resolve v2.0.0 CodeQL alerts and exclude README.ja.md/…](https://github.com/virgiliojr94/book-to-skill/commit/be9ccf9969f4ff9158c754463cb2b952e00e0511) | virgiliojr94 |
| 2026-11-19 | [ci: bump the github-actions group with 2 updates (#329)](https://github.com/virgiliojr94/book-to-skill/commit/b2778f3b66c269ebf9b413cfca26fe4b286e0c7c) | dependabot[bot] |
| 2026-11-19 | [fix(pdf): match letter-spaced outline chapter headings (#347)](https://github.com/virgiliojr94/book-to-skill/commit/65f9b1decc6a3d89cdf1ff9465b7bb1705c3c30e) | wangngo |
| 2026-11-19 | [docs: add Japanese README (#328)](https://github.com/virgiliojr94/book-to-skill/commit/be16a0ed97f8ce0ca036c74d5c392ddecab05521) | eltociear |
| 2026-11-19 | [chore: slim archives with export-ignore and compressed docs images (#…](https://github.com/virgiliojr94/book-to-skill/commit/942033c8d4861fec369b156beb12af7e3906a21b) | blazardsky |
| 2026-11-19 | [feat(extractor): detect Georgian (თავი) chapter headings (#325)](https://github.com/virgiliojr94/book-to-skill/commit/2ad4a8dc54fdcba3d76fe7e3b1442f09641f1c0d) | dex0shubham |
| 2026-11-19 | [feat(extractor): detect Arabic (الفصل/الباب) chapter headings (#346)](https://github.com/virgiliojr94/book-to-skill/commit/1dd0b1541eca11b1914846af9213beaea9b2dfe1) | dex0shubham |
| 2026-11-19 | [fix(epub): accept whitespace around XML attribute equals (#323)](https://github.com/virgiliojr94/book-to-skill/commit/5db008aa7a710206afda30760bedc58b34695076) | Stamina9 |

[See all commits ↗](https://github.com/virgiliojr94/book-to-skill/commits)

## ⬇️ Get it

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git
```
