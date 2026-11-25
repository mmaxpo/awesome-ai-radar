# oomol-lab/pdf-craft

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/oomol-lab/pdf-craft)

> PDF craft can convert PDF files into various other formats. This project will focus on processing PDF files of scanned books.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Scanned PDFs to Markdown or EPUB |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 6.8k |
| 🍴 **Forks** | 502 |
| 🐞 **Open issues + PRs** | [13](https://github.com/oomol-lab/pdf-craft/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `document` `ocr` `pdf` `deepseek-ocr` `book-digitization` `deepseek-ocr-2` `document-processing` `ebook` `epub` `epub-translation` `markdown` `pdf-converter` `pdf-parser` `pdf-to-epub` `pdf-to-markdown` `pdf-translation` `python` `scanned-pdf` `text-extraction` `translation` |
| 🕒 **Last activity** | 2026-11-23 (2d ago) |
| 📅 **Created** | 2025-02-12 |
| 📦 **Latest release** | [v2.6.7](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.7) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 38.0 MB |
| 🌐 **Website** | https://pdfcraft.ai |

## 📦 Recent releases

### [v2.6.7](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.7)
<sub>2026-10-28 · 28d ago</sub>

> **PDF Craft v2.6.7**
> Restore incremental PDF extraction `on_body` / `on_footnote` delivery after the
> 2.6.6 regression. Closed page-processed paragraphs and footnotes arrive while OCR and
> later analysis are still running, without a duplicate replay at completion.
> Page refinement now runs as a bounded pipeline: JEV starts when its initial
> neighbor inputs are ready; the target LLM follows only that page's score. Neighbor
> …

### [v2.6.6](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.6)
<sub>2026-10-28 · 28d ago</sub>

> **PDF Craft v2.6.6**
> PDF Craft 2.6.6 fixes concurrent PDF extraction, footnote OCR masks, XML fill
> whitespace recovery, and chapter consistency after refinement. Downstream content
> now comes from one finalized extraction result.
> **Migration from 2.6.5**
> - Extraction PAGE progress now uses stages **0–7** (`max_stage=7`). Update numeric
> …

### [v2.6.5](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.5)
<sub>2026-10-26 · 1mo ago</sub>

> **PDF Craft v2.6.5**
> PDF Craft 2.6.5 adds translation-size previews and operation-scoped resource
> reports, so applications can inspect source words before execution and observed
> remote consumption after completion, failure or cancellation.
> - New `pcex_words_count` and `epub_words_count` read-only queries share the actual
>   translation pre-scan and source-word rules. Matching options produce the same
> …

### [v2.6.4](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.4)
<sub>2026-10-26 · 1mo ago</sub>

> **PDF Craft v2.6.4**
> PDF Craft 2.6.4 unifies extraction and translation progress, counts source words
> consistently, and starts independent metadata and PCEX translation work as soon as
> its inputs are ready. This release includes breaking progress API changes; callback
> consumers should follow the migration notes below. PCEX v4 is unchanged.
> **Unified work-unit progress**
> …

### [v2.6.3](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.3)
<sub>2026-10-25 · 1mo ago</sub>

> **PDF Craft v2.6.3**
> PDF Craft 2.6.3 preserves the original cause of concurrent service failures,
> coordinates temporary rate limits across request pools, and replaces automatic
> PDF input gating with optional input assertions. It also fixes XML fill text
> handling and PDF-to-PCEX directory/chapter consistency during refinement and recovery.
> Operation-scoped request headers now propagate across model-service calls.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [docs: use PDF Craft logo in deployment options header SVG (#672)](https://github.com/oomol-lab/pdf-craft/commit/56acd2887ef78b12e2fe50abcbd5147ce14ce7e1) | alwaysmavs |
| 2026-11-23 | [docs: add 3-column deployment options table, MCP/OpenAPI badges, and …](https://github.com/oomol-lab/pdf-craft/commit/adf0abe052845fb575c6b3a81da069abbd90ca67) | alwaysmavs |
| 2026-11-20 | [fix: align MiniCPM-OCR with the upstream backend (#670)](https://github.com/oomol-lab/pdf-craft/commit/6eee49ae10622d66abd5191c6acae167398c6d5a) | Moskize91 |
| 2026-11-20 | [feat(ocr): add MiniCPM-OCR vendor backend (#669)](https://github.com/oomol-lab/pdf-craft/commit/cb47d557d5108548bc8f3136354ecbcbd01e423e) | Caldalis |
| 2026-11-19 | [Tag top online conversion links in three READMEs (#668)](https://github.com/oomol-lab/pdf-craft/commit/ecd36d215a8786f48aafde8df81126b69e1ce4b9) | Cheerego7 |
| 2026-11-18 | [chore: add pdfcraft.ai links to PyPI project URLs (#667)](https://github.com/oomol-lab/pdf-craft/commit/e755c82190ded3b5e9a3dc7b85af260b18f50d01) | l1shen |
| 2026-11-14 | [Localize the top online conversion links in two READMEs (#666)](https://github.com/oomol-lab/pdf-craft/commit/72375b2cc448891af54b6cde78cd8947fc50ed1a) | alwaysmavs |
| 2026-10-28 | [fix: finalize PDF layout from direct page dependencies (#568)](https://github.com/oomol-lab/pdf-craft/commit/46ac35d6b22b439f230f8a188bca7c230a763113) | Moskize91 |
| 2026-10-28 | [fix: deliver content callbacks and page progress without unrelated wa…](https://github.com/oomol-lab/pdf-craft/commit/6a11c2de2bc462f1a48400ceafd3f1b4f600d6be) | Moskize91 |
| 2026-10-28 | [fix: unblock ready OCR neighborhoods for page refinement (#566)](https://github.com/oomol-lab/pdf-craft/commit/7619abd4cc445c9f363b6ef26014c5c4094062a8) | Moskize91 |

[See all commits ↗](https://github.com/oomol-lab/pdf-craft/commits)

## ⬇️ Get it

```bash
git clone https://github.com/oomol-lab/pdf-craft.git
```
