# docling-project/docling

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/docling-project/docling)

> Get your documents ready for gen AI

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Convert PDFs/Office docs into AI-ready structured data (IBM) |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 71.1k |
| 🍴 **Forks** | 5.4k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/docling-project/docling/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `convert` `documents` `pdf` `tables` `document-parser` `document-parsing` `docx` `html` `markdown` `pdf-converter` `pdf-to-json` `pdf-to-text` `pptx` `xlsx` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2024-07-09 |
| 📦 **Latest release** | [v2.153.0](https://github.com/docling-project/docling/releases/tag/v2.153.0) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 479.8 MB |
| 🌐 **Website** | https://docling-project.github.io/docling |

## 📦 Recent releases

### [v2.153.0](https://github.com/docling-project/docling/releases/tag/v2.153.0)
<sub>2026-11-25 · today</sub>

> **Feature**
> * **pdf:** Expose docling-parse do_char_normalization in PdfBackendOptions ([#5541](https://github.com/docling-project/docling/issues/5541)) ([`3f95a7c`](https://github.com/docling-project/docling/commit/3f95a7cb6ff1f1841315c4b2a2dad6d63ae8a693))
> **Fix**
> * **email:** Follow-up fixes for the 'format=flowed' support ([#5557](https://github.com/docling-project/docling/issues/5557)) ([`0521b43`](https://github.com/docling-project/docling/commit/0521b4334488bfdaa76ecfcdc4a6db7d11792c44))
> * **uspto:** Put table cells with sub- or superscripts in rich cells ([#5236](https://github.com/docling-project/docling/issues/5236)) ([`ec4ac75`](https://github.com/docling-project/docling/commit/ec4ac75d24f81f8f71f855f91ad2c3c204946574))
> * **msword:** Keep the sign of a negative drawing position ([#4292](https://github.com/docling-project/docling/issues/4292)) ([`8dec7e1`](https://github.com/docling-project/docling/commit/8dec7e155e936911cac792cec56b2b01932b1b9c))
> …

### [v2.152.0](https://github.com/docling-project/docling/releases/tag/v2.152.0)
<sub>2026-11-23 · 3d ago</sub>

> **Feature**
> * **pdf:** Cancel queued PDF parsing when conversions stop ([#5456](https://github.com/docling-project/docling/issues/5456)) ([`4c0a96d`](https://github.com/docling-project/docling/commit/4c0a96de53af1032a2f2ac0375fdd7f844672349))
> * **service:** Let the server choose the default pipeline ([#4875](https://github.com/docling-project/docling/issues/4875)) ([`adfdff3`](https://github.com/docling-project/docling/commit/adfdff3426692a736145c3a3e0ac4fc837615d1e))
> * Turn audio/video transcripts and slide media into tracks ([#4752](https://github.com/docling-project/docling/issues/4752)) ([`5182e55`](https://github.com/docling-project/docling/commit/5182e556308958f3ac4762bb7d03a092c2f339c9))
> * **heading-hierarchy:** Read keyword markers of other languages ([#5474](https://github.com/docling-project/docling/issues/5474)) ([`557df04`](https://github.com/docling-project/docling/commit/557df045572672b4cf62a119c5252af49938a10b))
> * **vlm:** Add native MLX support for Nemotron 3.5 Parse ([#4934](https://github.com/docling-project/docling/issues/4934)) ([`825c774`](https://github.com/docling-project/docling/commit/825c77458b4d05ed7071d0789dc8e40ba9d18211))
> …

### [v2.151.1](https://github.com/docling-project/docling/releases/tag/v2.151.1)
<sub>2026-11-19 · 6d ago</sub>

> **Fix**
> * **service-client:** Keep the WebSocket poll fallback within the original timeout ([#5121](https://github.com/docling-project/docling/issues/5121)) ([`f9249e5`](https://github.com/docling-project/docling/commit/f9249e5067d7dacc01bd9a55abf5eb945b3861d0))
> * **service-client:** Propagate input iterator errors ([#5013](https://github.com/docling-project/docling/issues/5013)) ([`1150323`](https://github.com/docling-project/docling/commit/11503233cc174f6f7eedc32e2f03c46a93c69176))
> * Preserve VLM page-range provenance and verify complete assembly ([#4498](https://github.com/docling-project/docling/issues/4498)) ([`5068b03`](https://github.com/docling-project/docling/commit/5068b0365c347641fe51219dd9b754357aa32c93))
> * Avoid OpenCV FIPS aborts with Databricks opt-out setting ([#5430](https://github.com/docling-project/docling/issues/5430)) ([`de09f2a`](https://github.com/docling-project/docling/commit/de09f2a81460fb8439fc228d09d0faeeec48d301))
> * **docx:** Keep XML comments in NOTES, drop processing instructions ([#4584](https://github.com/docling-project/docling/issues/4584)) ([`f13a8bc`](https://github.com/docling-project/docling/commit/f13a8bc98532abcd7b306fd83d6486bc9afcddc2))
> …

### [v2.151.0](https://github.com/docling-project/docling/releases/tag/v2.151.0)
<sub>2026-11-19 · 7d ago</sub>

> **Feature**
> * **pptx:** Read waterfall, treemap and the other Office 2016 charts ([#5371](https://github.com/docling-project/docling/issues/5371)) ([`440492a`](https://github.com/docling-project/docling/commit/440492ac0d0e14952b32dda28fede7495611c899))
> * **email:** Add the events of calendar invitations ([#5357](https://github.com/docling-project/docling/issues/5357)) ([`6d3bb9e`](https://github.com/docling-project/docling/commit/6d3bb9ee1bffaee73f2dddfda10dc0f1c438a643))
> **Fix**
> * **pptx:** Limit the decompressed size of PPTX archive members ([#5113](https://github.com/docling-project/docling/issues/5113)) ([`587d121`](https://github.com/docling-project/docling/commit/587d12126dce2b931f105ca8c6a61cfc2b19fbf6))
> * **granite_vision:** Render table and chart crops at a configurable scale ([#5460](https://github.com/docling-project/docling/issues/5460)) ([`d1a7b7b`](https://github.com/docling-project/docling/commit/d1a7b7bfbed67d0a32e7c7a195722b6f5da20446))
> …

### [v2.150.1](https://github.com/docling-project/docling/releases/tag/v2.150.1)
<sub>2026-11-14 · 12d ago</sub>

> **Fix**
> * **cli:** Omit from_formats in convert-remote unless --from is set ([#5346](https://github.com/docling-project/docling/issues/5346)) ([`ebc50e3`](https://github.com/docling-project/docling/commit/ebc50e35057462c39771f28ca1d5c593e20a70c3))
> * **docx:** Detect headings from paragraph-level w:outlineLvl (#3312) ([#4129](https://github.com/docling-project/docling/issues/4129)) ([`31d14a7`](https://github.com/docling-project/docling/commit/31d14a74b7bddc850541ab8363b8585085845313))
> * **docx:** Keep hyperlink targets in footnotes and endnotes ([#5322](https://github.com/docling-project/docling/issues/5322)) ([`0c9a1cd`](https://github.com/docling-project/docling/commit/0c9a1cd372b49242065c7693dc0c60688733369b))
> * **docx:** Keep a single-cell table nested in a table cell inside the cell ([#5258](https://github.com/docling-project/docling/issues/5258)) ([`b9bf356`](https://github.com/docling-project/docling/commit/b9bf356f9763095ca9d51e7452a054a7db20f237))
> * **docx:** Close an open list before a table that follows it ([#5309](https://github.com/docling-project/docling/issues/5309)) ([`fec4dc3`](https://github.com/docling-project/docling/commit/fec4dc3b956db6701b7ae2bc6b28890bfd4008ee))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(ocr): make the Tesseract CLI DPI hint optional (#5564)](https://github.com/docling-project/docling/commit/9e196f7dc29c40afa8d229151d547fe494f6a306) | basilk15 |
| 2026-11-26 | [fix(email): keep display name of Exchange sender in .msg files (#5420)](https://github.com/docling-project/docling/commit/8a3c661fa16aa2dd8caec0a603259152d9269e79) | Kylinny |
| 2026-11-26 | [fix(email): strip trailing NUL characters from .msg properties and bo…](https://github.com/docling-project/docling/commit/490746a0d2f46cc5d50b93befc8978375e8a9fcf) | DhyaanKanoja11 |
| 2026-11-26 | [fix(mets): limit the TAR extended-header data read before each member…](https://github.com/docling-project/docling/commit/17285a883ef6d2b4e3407ce066f544649070129c) | dolfim-ibm |
| 2026-11-26 | [fix(pipeline): report incomplete slide media conversions (#5566)](https://github.com/docling-project/docling/commit/b2ac49643c8a43f74ca65bdef2776a32845275c2) | basilk15 |
| 2026-11-26 | [fix(cli): read .env for convert-remote only with --env-file or --dote…](https://github.com/docling-project/docling/commit/c9d52060e65a6c5cf0624674406c0e18b969d8cc) | dolfim-ibm |
| 2026-11-26 | [fix(pptx): keep chart series names stored as literal text (#5570)](https://github.com/docling-project/docling/commit/12974b3706b36e97874d30babfaf30f4bd1ba3d2) | kartsan03 |
| 2026-11-26 | [fix(latex): end a table row at \tabularnewline (#5560)](https://github.com/docling-project/docling/commit/6fceee6a36e3aab4ada28b0681dae3a5692fae3c) | leninworld |
| 2026-11-26 | [fix(docx): build heading numbers from the w:lvlText of the numbering …](https://github.com/docling-project/docling/commit/fd729a4892a04918fadd4680ab7c6971dc3ed608) | MartykQ |
| 2026-11-26 | [fix: limit the expansion of generic ZIP inputs by default (#5605)](https://github.com/docling-project/docling/commit/318cede4cfa2e4b05074bc6043288b5efa44af2a) | dolfim-ibm |

[See all commits ↗](https://github.com/docling-project/docling/commits)

## ⬇️ Get it

```bash
git clone https://github.com/docling-project/docling.git
```
