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
| ⭐ **Stars** | 39.0k |
| 🍴 **Forks** | 4.2k |
| 🐞 **Open issues + PRs** | [17](https://github.com/virgiliojr94/book-to-skill/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-agents` `context-engineering` `document-processing` `edtech` `knowledge-base` `knowledge-management` `llm` `pdf-to-markdown` `rag` `self-study` `study-tools` `book-to-skill` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-05-01 |
| 📦 **Latest release** | [v2.0.1](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.1) — 2026-11-19 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 3.1 MB |

## 📦 Recent releases

### [v2.0.1](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.1)
<sub>2026-11-19 · 5d ago</sub>

> **[2.0.1] - 2026-11-19**
> **Added**
> - Add opt-in guided MCP setup directly in Step 0
> - Detect Arabic (الفصل/الباب) chapter headings (#346)
> - Detect Georgian (თავი) chapter headings (#325)
> **Documentation**
> …

### [v2.0.0](https://github.com/virgiliojr94/book-to-skill/releases/tag/v2.0.0)
<sub>2026-11-19 · 6d ago</sub>

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
| 2026-11-24 | [chore(governance): enable issue-first enforcement mode on master (#360)](https://github.com/virgiliojr94/book-to-skill/commit/79b3fa66d249635453f8e9bc517fe033ac9d5a91) | virgiliojr94 |
| 2026-11-24 | [fix(ci): prevent receipt re-minting when an approved issue is edited …](https://github.com/virgiliojr94/book-to-skill/commit/feed26e60f9b2aa2ecd26ba1780bd3acac75b5d1) | virgiliojr94 |
| 2026-11-24 | [fix(ci): separate issue-first runner job name from status context (#360)](https://github.com/virgiliojr94/book-to-skill/commit/c5af014e5c2b83ba3b32bfe763a11f1a23ed87fd) | virgiliojr94 |
| 2026-11-24 | [chore(governance): add issue-first policy evaluator and workflow in o…](https://github.com/virgiliojr94/book-to-skill/commit/b2223089a09a2567543ed956c7875767787afc26) | virgiliojr94 |
| 2026-11-24 | [test(pdf): resolve CodeQL mutable-attribute import alert in image rep…](https://github.com/virgiliojr94/book-to-skill/commit/024b5c3c12d594f65b583ac8974008b7be3e0428) | virgiliojr94 |
| 2026-11-24 | [fix(epub): ignore commented XML package entries (#342)](https://github.com/virgiliojr94/book-to-skill/commit/4350de7b7a49c12853a66d5761ffeed99b013041) | Stamina9 |
| 2026-11-24 | [fix(pdf): decode pdfinfo output as UTF-8 (#344)](https://github.com/virgiliojr94/book-to-skill/commit/9c51da283373568e25c21604cdd3b03933118c68) | Stamina9 |
| 2026-11-24 | [fix(pdf): check later pages before rejecting scans (#354)](https://github.com/virgiliojr94/book-to-skill/commit/1bdf5c7351cc51a0da27999705ca6dbadfad17ea) | Stamina9 |
| 2026-11-24 | [fix(pdf): report embedded images that text extraction drops (#356)](https://github.com/virgiliojr94/book-to-skill/commit/e75d6ff2d5e25b4c93acb58f576556cf3be21c7e) | TanmayShah29 |
| 2026-11-24 | [ci: bump actions/dependency-review-action from 5.0.0 to 5.0.1 (#357)](https://github.com/virgiliojr94/book-to-skill/commit/aee998ca1ad8182bc9d56969b55ea54279ec2b04) | dependabot[bot] |

[See all commits ↗](https://github.com/virgiliojr94/book-to-skill/commits)

## ⬇️ Get it

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git
```
