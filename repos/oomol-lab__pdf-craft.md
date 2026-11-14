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
| ⭐ **Stars** | 6.7k |
| 🍴 **Forks** | 485 |
| 🐞 **Open issues + PRs** | [12](https://github.com/oomol-lab/pdf-craft/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `document` `ocr` `pdf` `deepseek-ocr` `book-digitization` `deepseek-ocr-2` `document-processing` `ebook` `epub` `epub-translation` `markdown` `pdf-converter` `pdf-parser` `pdf-to-epub` `pdf-to-markdown` `pdf-translation` `python` `scanned-pdf` `text-extraction` `translation` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2025-02-12 |
| 📦 **Latest release** | [v2.6.7](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.7) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 37.9 MB |
| 🌐 **Website** | https://pdfcraft.ai |

## 📦 Recent releases

### [v2.6.7](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.7)
<sub>2026-10-28 · 17d ago</sub>

> **PDF Craft v2.6.7**
> Restore incremental PDF extraction `on_body` / `on_footnote` delivery after the
> 2.6.6 regression. Closed page-processed paragraphs and footnotes arrive while OCR and
> later analysis are still running, without a duplicate replay at completion.
> Page refinement now runs as a bounded pipeline: JEV starts when its initial
> neighbor inputs are ready; the target LLM follows only that page's score. Neighbor
> …

### [v2.6.6](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.6)
<sub>2026-10-28 · 17d ago</sub>

> **PDF Craft v2.6.6**
> PDF Craft 2.6.6 fixes concurrent PDF extraction, footnote OCR masks, XML fill
> whitespace recovery, and chapter consistency after refinement. Downstream content
> now comes from one finalized extraction result.
> **Migration from 2.6.5**
> - Extraction PAGE progress now uses stages **0–7** (`max_stage=7`). Update numeric
> …

### [v2.6.5](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.5)
<sub>2026-10-26 · 19d ago</sub>

> **PDF Craft v2.6.5**
> PDF Craft 2.6.5 adds translation-size previews and operation-scoped resource
> reports, so applications can inspect source words before execution and observed
> remote consumption after completion, failure or cancellation.
> - New `pcex_words_count` and `epub_words_count` read-only queries share the actual
>   translation pre-scan and source-word rules. Matching options produce the same
> …

### [v2.6.4](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.4)
<sub>2026-10-26 · 19d ago</sub>

> **PDF Craft v2.6.4**
> PDF Craft 2.6.4 unifies extraction and translation progress, counts source words
> consistently, and starts independent metadata and PCEX translation work as soon as
> its inputs are ready. This release includes breaking progress API changes; callback
> consumers should follow the migration notes below. PCEX v4 is unchanged.
> **Unified work-unit progress**
> …

### [v2.6.3](https://github.com/oomol-lab/pdf-craft/releases/tag/v2.6.3)
<sub>2026-10-25 · 20d ago</sub>

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
| 2026-11-14 | [Localize the top online conversion links in two READMEs (#666)](https://github.com/oomol-lab/pdf-craft/commit/72375b2cc448891af54b6cde78cd8947fc50ed1a) | alwaysmavs |
| 2026-10-28 | [fix: finalize PDF layout from direct page dependencies (#568)](https://github.com/oomol-lab/pdf-craft/commit/46ac35d6b22b439f230f8a188bca7c230a763113) | Moskize91 |
| 2026-10-28 | [fix: deliver content callbacks and page progress without unrelated wa…](https://github.com/oomol-lab/pdf-craft/commit/6a11c2de2bc462f1a48400ceafd3f1b4f600d6be) | Moskize91 |
| 2026-10-28 | [fix: unblock ready OCR neighborhoods for page refinement (#566)](https://github.com/oomol-lab/pdf-craft/commit/7619abd4cc445c9f363b6ef26014c5c4094062a8) | Moskize91 |
| 2026-10-28 | [fix: stream PDF page refinement and incremental content delivery (#565)](https://github.com/oomol-lab/pdf-craft/commit/10579178437f06cc637eef793a4899cb93737445) | Moskize91 |
| 2026-10-28 | [fix: restore incremental extraction callbacks and prepare 2.6.7 (#564)](https://github.com/oomol-lab/pdf-craft/commit/8340f7c40aa4c643b06fec5af96d48ed1961739f) | Moskize91 |
| 2026-10-28 | [fix: prevent premature PCEX dependency release and callback terminati…](https://github.com/oomol-lab/pdf-craft/commit/d99c097e960b7eb54cf7bb35743a4fa9259e0f80) | Moskize91 |
| 2026-10-28 | [chore: prepare PDF Craft 2.6.6 release (#562)](https://github.com/oomol-lab/pdf-craft/commit/907ad581f00f280190e49083f19a990224e9670c) | Moskize91 |
| 2026-10-28 | [fix: finalize extraction semantics before downstream consumers (#561)](https://github.com/oomol-lab/pdf-craft/commit/4e098926a8ea5668bec88615a62faff31fef5bc7) | Moskize91 |
| 2026-10-28 | [fix: serialize extraction events and isolate blocking stream workers …](https://github.com/oomol-lab/pdf-craft/commit/0b06f964c251184f9b072a5683a66e75ef4062a8) | Moskize91 |

[See all commits ↗](https://github.com/oomol-lab/pdf-craft/commits)

## ⬇️ Get it

```bash
git clone https://github.com/oomol-lab/pdf-craft.git
```
