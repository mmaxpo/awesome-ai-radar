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
| 🐞 **Open issues + PRs** | [409](https://github.com/Unstructured-IO/unstructured/issues) |
| 💻 **Languages** | HTML 87% · Python 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `document-parsing` `machine-learning` `nlp` `ocr` `information-retrieval` `data-pipelines` `ml` `preprocessing` `pdf-to-text` `natural-language-processing` `pdf` `pdf-to-json` `document-image-analysis` `donut` `document-image-processing` `document-parser` `docx` `langchain` `llm` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2022-09-26 |
| 📦 **Latest release** | [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 232.2 MB |
| 🌐 **Website** | https://www.unstructured.io/ |

## 📦 Recent releases

### [0.27.37](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.37)
<sub>2026-11-06 · 7d ago</sub>

> **What's Changed**
> **Fixes**
> * fix(lang): keep the languages a caller passes on short ASCII text by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4601
> * fix(pdf): extract vector-heavy PDFs with the fast strategy instead of returning nothing by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4540
> * fix(cleaners): stop swapping en and em dashes in replace_unicode_quotes by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4654
> **Other changes**
> …

### [0.27.36](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.36)
<sub>2026-10-30 · 15d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: start 0.27.36-dev after 0.27.35 release by @ryannikolaidis in https://github.com/Unstructured-IO/unstructured/pull/4607
> * fix(xml): keep text that runs through child elements by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4573
> * fix(pptx): filter off-slide shapes by how much of the box is visible by @feiiiiii5 in https://github.com/Unstructured-IO/unstructured/pull/4604
> * fix(html_table): keep a declared rowspan of zero on empty cells by @Eapp1e in https://github.com/Unstructured-IO/unstructured/pull/4611
> …

### [0.27.35](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.35)
<sub>2026-10-27 · 18d ago</sub>

> **What's Changed**
> **Other changes**
> * chore: replace per-PR changelog edits with generated release notes by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4578
> * fix(utils): compare bounding boxes for elements with no page number by @simpleqt in https://github.com/Unstructured-IO/unstructured/pull/4561
> * fix(chunking): measure combine thresholds in tokens when max_tokens is set by @joaquinhuigomez in https://github.com/Unstructured-IO/unstructured/pull/4528
> * ci: guard release versions without blocking ordinary PRs by @cragwolfe in https://github.com/Unstructured-IO/unstructured/pull/4589
> …

### [0.27.34](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.34)
<sub>2026-10-22 · 22d ago</sub>

> **What's Changed**
> * perf: Free decode buffers sooner when restoring original elements by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4524
> * perf: Free image buffers sooner during figure extraction by @CyMule in https://github.com/Unstructured-IO/unstructured/pull/4523
> * fix: honor encoding= in partition_json and partition_ndjson by @linhongyu510 in https://github.com/Unstructured-IO/unstructured/pull/4483
> * fix(pptx): read a line break as a newline instead of a vertical tab by @L4XB in https://github.com/Unstructured-IO/unstructured/pull/4571
> * fix(email): drop the empty entry of an address group by @chrikrah in https://github.com/Unstructured-IO/unstructured/pull/4576
> …

### [0.27.33](https://github.com/Unstructured-IO/unstructured/releases/tag/0.27.33)
<sub>2026-10-22 · 23d ago</sub>

> **What's Changed**
> * fix(chunking): don't repeat a very large split element in every chunk by @kholdrex in https://github.com/Unstructured-IO/unstructured/pull/4565
> * fix(deps): bump certifi to 2026.10.19 by @lawrence-u10d in https://github.com/Unstructured-IO/unstructured/pull/4564
> **Full Changelog**: https://github.com/Unstructured-IO/unstructured/compare/0.27.32...0.27.33

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [fix(ci): repair partition benchmark dependencies (#4733)](https://github.com/Unstructured-IO/unstructured/commit/5390c569625e8e66254a55a6446757b2d2abe492) | cragwolfe |
| 2026-11-13 | [fix(partition): keep section parent_id after images and other non-tex…](https://github.com/Unstructured-IO/unstructured/commit/e1288ff734f7f42829adec18d17df2131c0e7da4) | kerthans |
| 2026-11-13 | [fix(csv): read a repeated header label as written (#4709)](https://github.com/Unstructured-IO/unstructured/commit/7d81b40ec51377b60c9731f4459d71b11dcde078) | Bensonluo |
| 2026-11-13 | [fix(metrics): preserve caller-owned detection predictions (#4702)](https://github.com/Unstructured-IO/unstructured/commit/ad56303cfae517612afcd5db85d3b4e303aa0d03) | Afloat16 |
| 2026-11-13 | [fix(metrics): separate threshold precision from the AP envelope (#4703)](https://github.com/Unstructured-IO/unstructured/commit/c47ef65e827f2b3d80a4bf246909d029dc8b4fe8) | Afloat16 |
| 2026-11-12 | [fix: produce no elements for an empty CSV or TSV file (#4707)](https://github.com/Unstructured-IO/unstructured/commit/0bf5f7875b8152eabd81f727625de3fa69d483e5) | Bensonluo |
| 2026-11-12 | [fix(lang): treat an empty language selection as automatic (#4704)](https://github.com/Unstructured-IO/unstructured/commit/5df7ea22dda26b8efa3ef6ea24153f7351bf3f00) | Afloat16 |
| 2026-11-12 | [chore: start 0.27.38-dev after 0.27.37 release (#4669)](https://github.com/Unstructured-IO/unstructured/commit/2da7d277a9e279da29672695811524415fc235dc) | ryannikolaidis |
| 2026-11-06 | [chore: release 0.27.37 (#4668)](https://github.com/Unstructured-IO/unstructured/commit/293d235cfcd5f5e89c3cc5ff85562005e182ae33) | qued |
| 2026-11-06 | [fix(cleaners): stop swapping en and em dashes in replace_unicode_quot…](https://github.com/Unstructured-IO/unstructured/commit/29bafea9467377812510ed83c24a0520655dbf57) | chrikrah |

[See all commits ↗](https://github.com/Unstructured-IO/unstructured/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Unstructured-IO/unstructured.git
```
