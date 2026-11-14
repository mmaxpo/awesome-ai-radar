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
| ⭐ **Stars** | 37.9k |
| 🍴 **Forks** | 4.0k |
| 🐞 **Open issues + PRs** | [30](https://github.com/virgiliojr94/book-to-skill/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-agents` `context-engineering` `document-processing` `edtech` `knowledge-base` `knowledge-management` `llm` `pdf-to-markdown` `rag` `self-study` `study-tools` `book-to-skill` |
| 🕒 **Last activity** | 2026-11-08 (5d ago) |
| 📅 **Created** | 2026-05-01 |
| 📦 **Latest release** | [v1.4.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v1.4.0) — 2026-08-10 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 2.4 MB |

## 📦 Recent releases

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
<sub>2026-06-17 · 4mo ago</sub>

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

### [v1.0.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v1.0.0)
<sub>2026-06-08 · 5mo ago</sub>

> **[1.0.0] — 2026-06-08**
> First formally tagged release. The converter is stable, multi-format, and
> validated on real books.
> **Added**
> - **Multi-format extraction** — PDF, EPUB, DOCX, HTML, Markdown, reStructuredText,
>   AsciiDoc, RTF, and MOBI/AZW/AZW3 (via Calibre), through a modular `extractor`
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-03 | [test(cli): add entry-point tests for cli.py and __main__.py (#90)](https://github.com/virgiliojr94/book-to-skill/commit/e7bb659d3261491c8b28793dcb9102fa64a46c22) | adwaitm1301 |
| 2026-11-03 | [refactor(tests): reduce detected test smells (#321)](https://github.com/virgiliojr94/book-to-skill/commit/1efc6f43833c2c7ab96b8d1245fdabff3054b8bd) | CarlaCristinaSA |
| 2026-11-03 | [fix(pdf): detect chapters from the PDF outline and record chapter lin…](https://github.com/virgiliojr94/book-to-skill/commit/182e1854782c2fce0e49af4f14c583e8c5a51673) | AminMortezaie |
| 2026-11-03 | [feat(pdf): add opt-in physical-page evidence sidecar (#307)](https://github.com/virgiliojr94/book-to-skill/commit/6a8b75694edf75ccb9ac0efa1935280f4aa64b30) | virgiliojr94 |
| 2026-11-03 | [feat(extractor): also detect Sinhala අධ්‍යාය chapter headings (#318)](https://github.com/virgiliojr94/book-to-skill/commit/9af24de500d0ee557832fb496b5080531992f6c5) | dex0shubham |
| 2026-11-03 | [feat(extractor): detect Armenian (Գլուխ) chapter headings (#314)](https://github.com/virgiliojr94/book-to-skill/commit/c41312b76e24a7e5c023195b589de64f2054ae53) | dex0shubham |
| 2026-11-03 | [fix(epub): decode container path XML references (#317)](https://github.com/virgiliojr94/book-to-skill/commit/9fb0dacdeff231773c76a73bdf8519d993f1b0f3) | Stamina9 |
| 2026-11-03 | [fix(rtf): preserve required line breaks in fallback (#313)](https://github.com/virgiliojr94/book-to-skill/commit/e330b131c3d798aa38c1ee32cb7d35885cdcb3cf) | Stamina9 |
| 2026-11-03 | [fix(epub): report text fallback in technical mode (#319)](https://github.com/virgiliojr94/book-to-skill/commit/fdb37c174e6226fc05079f3640e8ddda09f3725e) | teachershuang |
| 2026-10-28 | [fix(epub): decode UTF-16 XML in stdlib fallback (#311)](https://github.com/virgiliojr94/book-to-skill/commit/7540eefbe74933f5fc84c86becac52486b347778) | Stamina9 |

[See all commits ↗](https://github.com/virgiliojr94/book-to-skill/commits)

## ⬇️ Get it

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git
```
