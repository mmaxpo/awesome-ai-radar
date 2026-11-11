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
| ⭐ **Stars** | 15.7k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [362](https://github.com/Unstructured-IO/unstructured/issues) |
| 💻 **Languages** | HTML 87% · Python 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `document-parsing` `machine-learning` `nlp` `ocr` `information-retrieval` `data-pipelines` `ml` `preprocessing` `pdf-to-text` `natural-language-processing` `pdf` `pdf-to-json` `document-image-analysis` `donut` `document-image-processing` `document-parser` `docx` `langchain` `llm` |
| 🕒 **Last activity** | 2026-11-06 (4d ago) |
| 📅 **Created** | 2022-09-26 |
| 📦 **Latest release** | [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 232.2 MB |
| 🌐 **Website** | https://www.unstructured.io/ |

## 📦 Recent releases

### [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37)
<sub>2026-11-06 · 4d ago</sub>

> **What's Changed**
> **Fixes**
> * fix(lang): keep the languages a caller passes on short ASCII text by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4601
> * fix(pdf): extract vector-heavy PDFs with the fast strategy instead of returning nothing by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4540
> * fix(cleaners): stop swapping en and em dashes in replace_unicode_quotes by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4654
> **Other changes**
> …

### [0.27.36](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.36)
<sub>2026-10-30 · 12d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: start 0.27.36-dev after 0.27.35 release by @ryannikolaidis in https://github.com/Unstructured-IO/unstructured/pull/4607
> * fix(xml): keep text that runs through child elements by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4573
> * fix(pptx): filter off-slide shapes by how much of the box is visible by @feiiiiii5 in https://github.com/Unstructured-IO/unstructured/pull/4604
> * fix(html_table): keep a declared rowspan of zero on empty cells by @Eapp1e in https://github.com/Unstructured-IO/unstructured/pull/4611
> …

### [0.27.35](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.35)
<sub>2026-10-27 · 15d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: replace per-PR changelog edits with generated release notes by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4578
> * fix(utils): compare bounding boxes for elements with no page number by @simpleqt in https://github.com/Unstructured-IO/unstructured/pull/4561
> * fix(chunking): measure combine thresholds in tokens when max_tokens is set by @joaquinhuigomez in https://github.com/Unstructured-IO/unstructured/pull/4528
> * ci: guard release versions without blocking ordinary PRs by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4589
> …

### [0.27.34](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.34)
<sub>2026-10-22 · 19d ago</sub>

> **What's Changed**
> * perf: Free decode buffers sooner when restoring original elements by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4524
> * perf: Free image buffers sooner during figure extraction by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4523
> * fix: honor encoding= in partition_json and partition_ndjson by @linhongyu510 in https://github.com/Unstructured-IO/unstructured/pull/4483
> * fix(pptx): read a line break as a newline instead of a vertical tab by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4571
> * fix(email): drop the empty entry of an address group by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4576
> …

### [0.27.33](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.33)
<sub>2026-10-22 · 20d ago</sub>

> **What's Changed**
> * fix(chunking): don't repeat a very large split element in every chunk by @kholdrex in https://github.com/Unstructured-IO/unstructured/pull/4565
> * fix(deps): bump certifi to 2026.10.19 by @lawrence-u10d in https://github.com/Unstructured-IO/unstructured/pull/4564
> **Full Changelog**: https://github.com/Unstructured-IO/unstructured/compare/0.27.32...0.27.33

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-06 | [chore: release 0.27.37 (#4668)](https://github.com/Unstructured-IO/unstructured/commit/293d235cfcd5f5e89c3cc5ff85562005e182ae33) | qued |
| 2026-11-06 | [fix(cleaners): stop swapping en and em dashes in replace_unicode_quot…](https://github.com/Unstructured-IO/unstructured/commit/29bafea9467377812510ed83c24a0520655dbf57) | chrikrah |
| 2026-11-06 | [fix(coordinates): default CoordinateSystem.orientation to CARTESIAN (…](https://github.com/Unstructured-IO/unstructured/commit/3cfcf4f5ab5b90f08ef0251851b41cdc81450c0b) | Eapp1e |
| 2026-11-06 | [fix(documents): count the hash-id sequence number per page, not per c…](https://github.com/Unstructured-IO/unstructured/commit/9b626895ba4d41c2796044f38878854673fea0de) | Eapp1e |
| 2026-11-04 | [fix(docx): keep text that python-docx skips inside wrapper elements (…](https://github.com/Unstructured-IO/unstructured/commit/582baf66ac056e48ed1d348b967bf2228f747bdb) | qued |
| 2026-11-03 | [fix(pdf): extract vector-heavy PDFs with the fast strategy instead of…](https://github.com/Unstructured-IO/unstructured/commit/d505b6010964de066a33fcce716a644e5887e7d3) | CyMule |
| 2026-11-02 | [fix(json): accept non-seekable streams while preserving legacy adapte…](https://github.com/Unstructured-IO/unstructured/commit/acc984515fca358831bc67dc5ea4ca61071a203e) | Zhi-Xiang-Guo |
| 2026-10-30 | [fix(html): render each Title at its own heading level in elements_to_…](https://github.com/Unstructured-IO/unstructured/commit/910d9f41e70a17e561797106ef4b9096a8554254) | tanishqbaweja |
| 2026-10-30 | [fix(deps): require filelock>=4.2.1 for GHSA-v4x8-3wr5-3wq8 (#4628)](https://github.com/Unstructured-IO/unstructured/commit/6c304a9605c867223359a9db82d3ca382f7af1b5) | tanishqbaweja |
| 2026-10-30 | [fix(lang): keep the languages a caller passes on short ASCII text (#4…](https://github.com/Unstructured-IO/unstructured/commit/e43c6da62960d30da4665827b264c60371d6a5dc) | chrikrah |

[See all commits ↗](https://github.com/Unstructured-IO/unstructured/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Unstructured-IO/unstructured.git
```
