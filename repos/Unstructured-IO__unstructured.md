# Unstructured-IO/unstructured

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Unstructured-IO/unstructured)

> Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Parse PDFs, Word, HTML etc. into clean chunks for LLMs |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 15.8k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [454](https://github.com/Unstructured-IO/unstructured/issues) |
| 💻 **Languages** | HTML 87% · Python 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `document-parsing` `machine-learning` `nlp` `ocr` `information-retrieval` `data-pipelines` `ml` `preprocessing` `pdf-to-text` `natural-language-processing` `pdf` `pdf-to-json` `document-image-analysis` `donut` `document-image-processing` `document-parser` `docx` `langchain` `llm` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2022-09-26 |
| 📦 **Latest release** | [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 236.4 MB |
| 🌐 **Website** | https://www.unstructured.io/ |

## 📦 Recent releases

### [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37)
<sub>2026-11-06 · 11d ago</sub>

> **What's Changed**
> **Fixes**
> * fix(lang): keep the languages a caller passes on short ASCII text by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4601
> * fix(pdf): extract vector-heavy PDFs with the fast strategy instead of returning nothing by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4540
> * fix(cleaners): stop swapping en and em dashes in replace_unicode_quotes by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4654
> **Other changes**
> …

### [0.27.36](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.36)
<sub>2026-10-30 · 19d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: start 0.27.36-dev after 0.27.35 release by @ryannikolaidis in https://github.com/Unstructured-IO/unstructured/pull/4607
> * fix(xml): keep text that runs through child elements by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4573
> * fix(pptx): filter off-slide shapes by how much of the box is visible by @feiiiiii5 in https://github.com/Unstructured-IO/unstructured/pull/4604
> * fix(html_table): keep a declared rowspan of zero on empty cells by @Eapp1e in https://github.com/Unstructured-IO/unstructured/pull/4611
> …

### [0.27.35](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.35)
<sub>2026-10-27 · 22d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: replace per-PR changelog edits with generated release notes by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4578
> * fix(utils): compare bounding boxes for elements with no page number by @simpleqt in https://github.com/Unstructured-IO/unstructured/pull/4561
> * fix(chunking): measure combine thresholds in tokens when max_tokens is set by @joaquinhuigomez in https://github.com/Unstructured-IO/unstructured/pull/4528
> * ci: guard release versions without blocking ordinary PRs by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4589
> …

### [0.27.34](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.34)
<sub>2026-10-22 · 26d ago</sub>

> **What's Changed**
> * perf: Free decode buffers sooner when restoring original elements by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4524
> * perf: Free image buffers sooner during figure extraction by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4523
> * fix: honor encoding= in partition_json and partition_ndjson by @linhongyu510 in https://github.com/Unstructured-IO/unstructured/pull/4483
> * fix(pptx): read a line break as a newline instead of a vertical tab by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4571
> * fix(email): drop the empty entry of an address group by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4576
> …

### [0.27.33](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.33)
<sub>2026-10-22 · 27d ago</sub>

> **What's Changed**
> * fix(chunking): don't repeat a very large split element in every chunk by @kholdrex in https://github.com/Unstructured-IO/unstructured/pull/4565
> * fix(deps): bump certifi to 2026.10.19 by @lawrence-u10d in https://github.com/Unstructured-IO/unstructured/pull/4564
> **Full Changelog**: https://github.com/Unstructured-IO/unstructured/compare/0.27.32...0.27.33

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [perf: stop text extraction after finding the requested match (#4780)](https://github.com/Unstructured-IO/unstructured/commit/52735431453043da0f3225b1fdd3d20b15c71b91) | Afloat16 |
| 2026-11-17 | [perf(sorting): accumulate dense XY-cut projections once (#4748)](https://github.com/Unstructured-IO/unstructured/commit/230ed8b27ad1ebbca3ef6e8b41d4b87ccbe3e941) | Afloat16 |
| 2026-11-17 | [perf(chunking): avoid repeated table scans while forming chunks (#4744)](https://github.com/Unstructured-IO/unstructured/commit/cb686ff9180afcc7bb6db43acd6aca8f3dc16e9c) | Afloat16 |
| 2026-11-17 | [perf(ocr): reuse paragraph index masks while grouping words (#4721)](https://github.com/Unstructured-IO/unstructured/commit/5bd1be5ed449d865f2daa9d4d28cfbc415300589) | Afloat16 |
| 2026-11-17 | [fix: strip leading UTF-8 BOM before JSON content-shape detection (#4397)](https://github.com/Unstructured-IO/unstructured/commit/0c166fc21b65de8d398ff3ba13976882266916a4) | chuenchen309 |
| 2026-11-17 | [fix: retain coordinates when classifying text as an email address (#4…](https://github.com/Unstructured-IO/unstructured/commit/d63cf141c2d70f61baad31939bbbeed501dcb5e4) | Afloat16 |
| 2026-11-17 | [fix: preserve repeated quoted CSV headers without a final newline (#4…](https://github.com/Unstructured-IO/unstructured/commit/08c7eb14529eee26c866a6fb3c56a78e36ef01b6) | Afloat16 |
| 2026-11-16 | [fix(csv): decompress a compressed CSV file named for its compression …](https://github.com/Unstructured-IO/unstructured/commit/3552529a5070ed1a4000c31846736aaa53a3f8bd) | Bensonluo |
| 2026-11-14 | [fix(chunking): don't emit a chunk that holds only the overlap when ov…](https://github.com/Unstructured-IO/unstructured/commit/ac932052e6e0ba3feab8a6e96b6d4480218e009f) | sinnercode228 |
| 2026-11-14 | [fix(ci): repair partition benchmark dependencies (#4733)](https://github.com/Unstructured-IO/unstructured/commit/5390c569625e8e66254a55a6446757b2d2abe492) | cragwolfe |

[See all commits ↗](https://github.com/Unstructured-IO/unstructured/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Unstructured-IO/unstructured.git
```
