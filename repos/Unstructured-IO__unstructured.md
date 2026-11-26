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
| 🐞 **Open issues + PRs** | [493](https://github.com/Unstructured-IO/unstructured/issues) |
| 💻 **Languages** | HTML 87% · Python 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `document-parsing` `machine-learning` `nlp` `ocr` `information-retrieval` `data-pipelines` `ml` `preprocessing` `pdf-to-text` `natural-language-processing` `pdf` `pdf-to-json` `document-image-analysis` `donut` `document-image-processing` `document-parser` `docx` `langchain` `llm` |
| 🕒 **Last activity** | 2026-11-24 (yesterday) |
| 📅 **Created** | 2022-09-26 |
| 📦 **Latest release** | [0.27.38](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.38) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 236.4 MB |
| 🌐 **Website** | https://www.unstructured.io/ |

## 📦 Recent releases

### [0.27.38](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.38)
<sub>2026-11-24 · yesterday</sub>

> **What's Changed**
> **Enhancements**
> * perf: render the PDF once in hi_res instead of once per pipeline stage by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4530
> **Fixes**
> * fix: produce no elements for an empty CSV or TSV file by @Bensonluo in https://github.com/Unstructured-IO/unstructured/pull/4707
> * fix(metrics): separate threshold precision from the AP envelope by @Afloat16 in https://github.com/Unstructured-IO/unstructured/pull/4703
> …

### [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37)
<sub>2026-11-06 · 19d ago</sub>

> **What's Changed**
> **Fixes**
> * fix(lang): keep the languages a caller passes on short ASCII text by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4601
> * fix(pdf): extract vector-heavy PDFs with the fast strategy instead of returning nothing by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4540
> * fix(cleaners): stop swapping en and em dashes in replace_unicode_quotes by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4654
> **Other changes**
> …

### [0.27.36](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.36)
<sub>2026-10-30 · 27d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: start 0.27.36-dev after 0.27.35 release by @ryannikolaidis in https://github.com/Unstructured-IO/unstructured/pull/4607
> * fix(xml): keep text that runs through child elements by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4573
> * fix(pptx): filter off-slide shapes by how much of the box is visible by @feiiiiii5 in https://github.com/Unstructured-IO/unstructured/pull/4604
> * fix(html_table): keep a declared rowspan of zero on empty cells by @Eapp1e in https://github.com/Unstructured-IO/unstructured/pull/4611
> …

### [0.27.35](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.35)
<sub>2026-10-27 · 1mo ago</sub>

> **What's Changed**
> **Other changes**
> * chore: replace per-PR changelog edits with generated release notes by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4578
> * fix(utils): compare bounding boxes for elements with no page number by @simpleqt in https://github.com/Unstructured-IO/unstructured/pull/4561
> * fix(chunking): measure combine thresholds in tokens when max_tokens is set by @joaquinhuigomez in https://github.com/Unstructured-IO/unstructured/pull/4528
> * ci: guard release versions without blocking ordinary PRs by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4589
> …

### [0.27.34](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.34)
<sub>2026-10-22 · 1mo ago</sub>

> **What's Changed**
> * perf: Free decode buffers sooner when restoring original elements by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4524
> * perf: Free image buffers sooner during figure extraction by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4523
> * fix: honor encoding= in partition_json and partition_ndjson by @linhongyu510 in https://github.com/Unstructured-IO/unstructured/pull/4483
> * fix(pptx): read a line break as a newline instead of a vertical tab by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4571
> * fix(email): drop the empty entry of an address group by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4576
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore: release 0.27.38 (#4854)](https://github.com/Unstructured-IO/unstructured/commit/2653935aa783e72b89b345cf63a74324962cdd75) | CyMule |
| 2026-11-24 | [perf: render the PDF once in hi_res instead of once per pipeline stag…](https://github.com/Unstructured-IO/unstructured/commit/2f685ec3d25f3bb58b64ee82666a1c0f79033407) | CyMule |
| 2026-11-19 | [fix(docx): stop long vertical merges from dropping table rows from te…](https://github.com/Unstructured-IO/unstructured/commit/1ab3be89b689fbe91a2152b720908b7edb143945) | inchang-ing |
| 2026-11-17 | [perf: stop text extraction after finding the requested match (#4780)](https://github.com/Unstructured-IO/unstructured/commit/52735431453043da0f3225b1fdd3d20b15c71b91) | Afloat16 |
| 2026-11-17 | [perf(sorting): accumulate dense XY-cut projections once (#4748)](https://github.com/Unstructured-IO/unstructured/commit/230ed8b27ad1ebbca3ef6e8b41d4b87ccbe3e941) | Afloat16 |
| 2026-11-17 | [perf(chunking): avoid repeated table scans while forming chunks (#4744)](https://github.com/Unstructured-IO/unstructured/commit/cb686ff9180afcc7bb6db43acd6aca8f3dc16e9c) | Afloat16 |
| 2026-11-17 | [perf(ocr): reuse paragraph index masks while grouping words (#4721)](https://github.com/Unstructured-IO/unstructured/commit/5bd1be5ed449d865f2daa9d4d28cfbc415300589) | Afloat16 |
| 2026-11-17 | [fix: strip leading UTF-8 BOM before JSON content-shape detection (#4397)](https://github.com/Unstructured-IO/unstructured/commit/0c166fc21b65de8d398ff3ba13976882266916a4) | chuenchen309 |
| 2026-11-17 | [fix: retain coordinates when classifying text as an email address (#4…](https://github.com/Unstructured-IO/unstructured/commit/d63cf141c2d70f61baad31939bbbeed501dcb5e4) | Afloat16 |
| 2026-11-17 | [fix: preserve repeated quoted CSV headers without a final newline (#4…](https://github.com/Unstructured-IO/unstructured/commit/08c7eb14529eee26c866a6fb3c56a78e36ef01b6) | Afloat16 |

[See all commits ↗](https://github.com/Unstructured-IO/unstructured/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Unstructured-IO/unstructured.git
```
