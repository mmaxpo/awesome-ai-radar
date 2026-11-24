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
| ⭐ **Stars** | 71.0k |
| 🍴 **Forks** | 5.4k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/docling-project/docling/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `convert` `documents` `pdf` `tables` `document-parser` `document-parsing` `docx` `html` `markdown` `pdf-converter` `pdf-to-json` `pdf-to-text` `pptx` `xlsx` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2024-07-09 |
| 📦 **Latest release** | [v2.152.0](https://github.com/docling-project/docling/releases/tag/v2.152.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 478.3 MB |
| 🌐 **Website** | https://docling-project.github.io/docling |

## 📦 Recent releases

### [v2.152.0](https://github.com/docling-project/docling/releases/tag/v2.152.0)
<sub>2026-11-23 · yesterday</sub>

> **Feature**
> * **pdf:** Cancel queued PDF parsing when conversions stop ([#5456](https://github.com/docling-project/docling/issues/5456)) ([`4c0a96d`](https://github.com/docling-project/docling/commit/4c0a96de53af1032a2f2ac0375fdd7f844672349))
> * **service:** Let the server choose the default pipeline ([#4875](https://github.com/docling-project/docling/issues/4875)) ([`adfdff3`](https://github.com/docling-project/docling/commit/adfdff3426692a736145c3a3e0ac4fc837615d1e))
> * Turn audio/video transcripts and slide media into tracks ([#4752](https://github.com/docling-project/docling/issues/4752)) ([`5182e55`](https://github.com/docling-project/docling/commit/5182e556308958f3ac4762bb7d03a092c2f339c9))
> * **heading-hierarchy:** Read keyword markers of other languages ([#5474](https://github.com/docling-project/docling/issues/5474)) ([`557df04`](https://github.com/docling-project/docling/commit/557df045572672b4cf62a119c5252af49938a10b))
> * **vlm:** Add native MLX support for Nemotron 3.5 Parse ([#4934](https://github.com/docling-project/docling/issues/4934)) ([`825c774`](https://github.com/docling-project/docling/commit/825c77458b4d05ed7071d0789dc8e40ba9d18211))
> …

### [v2.151.1](https://github.com/docling-project/docling/releases/tag/v2.151.1)
<sub>2026-11-19 · 5d ago</sub>

> **Fix**
> * **service-client:** Keep the WebSocket poll fallback within the original timeout ([#5121](https://github.com/docling-project/docling/issues/5121)) ([`f9249e5`](https://github.com/docling-project/docling/commit/f9249e5067d7dacc01bd9a55abf5eb945b3861d0))
> * **service-client:** Propagate input iterator errors ([#5013](https://github.com/docling-project/docling/issues/5013)) ([`1150323`](https://github.com/docling-project/docling/commit/11503233cc174f6f7eedc32e2f03c46a93c69176))
> * Preserve VLM page-range provenance and verify complete assembly ([#4498](https://github.com/docling-project/docling/issues/4498)) ([`5068b03`](https://github.com/docling-project/docling/commit/5068b0365c347641fe51219dd9b754357aa32c93))
> * Avoid OpenCV FIPS aborts with Databricks opt-out setting ([#5430](https://github.com/docling-project/docling/issues/5430)) ([`de09f2a`](https://github.com/docling-project/docling/commit/de09f2a81460fb8439fc228d09d0faeeec48d301))
> * **docx:** Keep XML comments in NOTES, drop processing instructions ([#4584](https://github.com/docling-project/docling/issues/4584)) ([`f13a8bc`](https://github.com/docling-project/docling/commit/f13a8bc98532abcd7b306fd83d6486bc9afcddc2))
> …

### [v2.151.0](https://github.com/docling-project/docling/releases/tag/v2.151.0)
<sub>2026-11-19 · 5d ago</sub>

> **Feature**
> * **pptx:** Read waterfall, treemap and the other Office 2016 charts ([#5371](https://github.com/docling-project/docling/issues/5371)) ([`440492a`](https://github.com/docling-project/docling/commit/440492ac0d0e14952b32dda28fede7495611c899))
> * **email:** Add the events of calendar invitations ([#5357](https://github.com/docling-project/docling/issues/5357)) ([`6d3bb9e`](https://github.com/docling-project/docling/commit/6d3bb9ee1bffaee73f2dddfda10dc0f1c438a643))
> **Fix**
> * **pptx:** Limit the decompressed size of PPTX archive members ([#5113](https://github.com/docling-project/docling/issues/5113)) ([`587d121`](https://github.com/docling-project/docling/commit/587d12126dce2b931f105ca8c6a61cfc2b19fbf6))
> * **granite_vision:** Render table and chart crops at a configurable scale ([#5460](https://github.com/docling-project/docling/issues/5460)) ([`d1a7b7b`](https://github.com/docling-project/docling/commit/d1a7b7bfbed67d0a32e7c7a195722b6f5da20446))
> …

### [v2.150.1](https://github.com/docling-project/docling/releases/tag/v2.150.1)
<sub>2026-11-14 · 10d ago</sub>

> **Fix**
> * **cli:** Omit from_formats in convert-remote unless --from is set ([#5346](https://github.com/docling-project/docling/issues/5346)) ([`ebc50e3`](https://github.com/docling-project/docling/commit/ebc50e35057462c39771f28ca1d5c593e20a70c3))
> * **docx:** Detect headings from paragraph-level w:outlineLvl (#3312) ([#4129](https://github.com/docling-project/docling/issues/4129)) ([`31d14a7`](https://github.com/docling-project/docling/commit/31d14a74b7bddc850541ab8363b8585085845313))
> * **docx:** Keep hyperlink targets in footnotes and endnotes ([#5322](https://github.com/docling-project/docling/issues/5322)) ([`0c9a1cd`](https://github.com/docling-project/docling/commit/0c9a1cd372b49242065c7693dc0c60688733369b))
> * **docx:** Keep a single-cell table nested in a table cell inside the cell ([#5258](https://github.com/docling-project/docling/issues/5258)) ([`b9bf356`](https://github.com/docling-project/docling/commit/b9bf356f9763095ca9d51e7452a054a7db20f237))
> * **docx:** Close an open list before a table that follows it ([#5309](https://github.com/docling-project/docling/issues/5309)) ([`fec4dc3`](https://github.com/docling-project/docling/commit/fec4dc3b956db6701b7ae2bc6b28890bfd4008ee))
> …

### [v2.150.0](https://github.com/docling-project/docling/releases/tag/v2.150.0)
<sub>2026-11-10 · 14d ago</sub>

> **Feature**
> * **xbrl:** Support iXBRL input and remote taxonomy resolution with source_uri ([#4689](https://github.com/docling-project/docling/issues/4689)) ([`43c016c`](https://github.com/docling-project/docling/commit/43c016caedf076b3016fe6cdd4ec4d2b53b5acc1))
> **Fix**
> * **email:** Preserve furniture from HTML message bodies ([#5228](https://github.com/docling-project/docling/issues/5228)) ([`75a7dbc`](https://github.com/docling-project/docling/commit/75a7dbc75caadddbdb1c283c8141fb1857ff8bc6))
> * **odf:** Show the displayed text of typed table cells ([#5232](https://github.com/docling-project/docling/issues/5232)) ([`b92f77c`](https://github.com/docling-project/docling/commit/b92f77cfcddd31ad5d849d9eef02072b43c51d45))
> * **example:** Avoid exposing original PII by default ([#5182](https://github.com/docling-project/docling/issues/5182)) ([`e77fcc2`](https://github.com/docling-project/docling/commit/e77fcc22863cca3097a1cb20c0496e83ef831c18))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [perf(table-structure): skip the TableFormer decode for a table that h…](https://github.com/docling-project/docling/commit/22b80a43d1baf8f7d51ae9b690e33b917a983ff4) | galer1us |
| 2026-11-24 | [fix(email): join the soft line breaks of format=flowed text (#5500)](https://github.com/docling-project/docling/commit/240f4606159d599e3dd04d816d26ff2ca6797ddf) | gagan-baghel |
| 2026-11-24 | [fix(pdf): report missing pages in the native pipeline (#5554)](https://github.com/docling-project/docling/commit/942df62435bbeb9e6db3de571366ab16332e029c) | xixi-box |
| 2026-11-24 | [feat(pdf): expose docling-parse do_char_normalization in PdfBackendOp…](https://github.com/docling-project/docling/commit/3f95a7cb6ff1f1841315c4b2a2dad6d63ae8a693) | galer1us |
| 2026-11-24 | [fix(calendar): do not describe days that BYMONTHDAY limits as every s…](https://github.com/docling-project/docling/commit/f969d7952482c700baad62b46cba7d5531c63578) | leninworld |
| 2026-11-24 | [fix(reading-order): compare merge candidates with the chain's tail (#…](https://github.com/docling-project/docling/commit/d615996c6064f17cd42843eabdb3d511b04b12b0) | nicdeluc |
| 2026-11-24 | [fix(calendar): keep the end when the start cannot be read (#5553)](https://github.com/docling-project/docling/commit/f170d86766f66ba5dc8d654ae76d6ea63b342e56) | hktitof |
| 2026-11-24 | [fix(html): keep the content of a details tag inside its table cell (#…](https://github.com/docling-project/docling/commit/7885a9c43d58f9f2c229ace102d642252794e599) | shlokbam |
| 2026-11-24 | [fix(latex): drop the empty row after the last table row (#5504)](https://github.com/docling-project/docling/commit/9605134f5f3defddf1b2dd1e4b39f8c854154b3b) | chuenchen309 |
| 2026-11-24 | [docs: describe PictureDescriptionApiOptions.params as JSON body field…](https://github.com/docling-project/docling/commit/730366ebe3e71faafc644dac4f7577bb3b612f8d) | thejesh23 |

[See all commits ↗](https://github.com/docling-project/docling/commits)

## ⬇️ Get it

```bash
git clone https://github.com/docling-project/docling.git
```
