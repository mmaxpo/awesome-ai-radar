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
| ⭐ **Stars** | 70.9k |
| 🍴 **Forks** | 5.4k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/docling-project/docling/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `convert` `documents` `pdf` `tables` `document-parser` `document-parsing` `docx` `html` `markdown` `pdf-converter` `pdf-to-json` `pdf-to-text` `pptx` `xlsx` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2024-07-09 |
| 📦 **Latest release** | [v2.152.0](https://github.com/docling-project/docling/releases/tag/v2.152.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 472.1 MB |
| 🌐 **Website** | https://docling-project.github.io/docling |

## 📦 Recent releases

### [v2.152.0](https://github.com/docling-project/docling/releases/tag/v2.152.0)
<sub>2026-11-23 · today</sub>

> **Feature**
> * **pdf:** Cancel queued PDF parsing when conversions stop ([#5456](https://github.com/docling-project/docling/issues/5456)) ([`4c0a96d`](https://github.com/docling-project/docling/commit/4c0a96de53af1032a2f2ac0375fdd7f844672349))
> * **service:** Let the server choose the default pipeline ([#4875](https://github.com/docling-project/docling/issues/4875)) ([`adfdff3`](https://github.com/docling-project/docling/commit/adfdff3426692a736145c3a3e0ac4fc837615d1e))
> * Turn audio/video transcripts and slide media into tracks ([#4752](https://github.com/docling-project/docling/issues/4752)) ([`5182e55`](https://github.com/docling-project/docling/commit/5182e556308958f3ac4762bb7d03a092c2f339c9))
> * **heading-hierarchy:** Read keyword markers of other languages ([#5474](https://github.com/docling-project/docling/issues/5474)) ([`557df04`](https://github.com/docling-project/docling/commit/557df045572672b4cf62a119c5252af49938a10b))
> * **vlm:** Add native MLX support for Nemotron 3.5 Parse ([#4934](https://github.com/docling-project/docling/issues/4934)) ([`825c774`](https://github.com/docling-project/docling/commit/825c77458b4d05ed7071d0789dc8e40ba9d18211))
> …

### [v2.151.1](https://github.com/docling-project/docling/releases/tag/v2.151.1)
<sub>2026-11-19 · 4d ago</sub>

> **Fix**
> * **service-client:** Keep the WebSocket poll fallback within the original timeout ([#5121](https://github.com/docling-project/docling/issues/5121)) ([`f9249e5`](https://github.com/docling-project/docling/commit/f9249e5067d7dacc01bd9a55abf5eb945b3861d0))
> * **service-client:** Propagate input iterator errors ([#5013](https://github.com/docling-project/docling/issues/5013)) ([`1150323`](https://github.com/docling-project/docling/commit/11503233cc174f6f7eedc32e2f03c46a93c69176))
> * Preserve VLM page-range provenance and verify complete assembly ([#4498](https://github.com/docling-project/docling/issues/4498)) ([`5068b03`](https://github.com/docling-project/docling/commit/5068b0365c347641fe51219dd9b754357aa32c93))
> * Avoid OpenCV FIPS aborts with Databricks opt-out setting ([#5430](https://github.com/docling-project/docling/issues/5430)) ([`de09f2a`](https://github.com/docling-project/docling/commit/de09f2a81460fb8439fc228d09d0faeeec48d301))
> * **docx:** Keep XML comments in NOTES, drop processing instructions ([#4584](https://github.com/docling-project/docling/issues/4584)) ([`f13a8bc`](https://github.com/docling-project/docling/commit/f13a8bc98532abcd7b306fd83d6486bc9afcddc2))
> …

### [v2.151.0](https://github.com/docling-project/docling/releases/tag/v2.151.0)
<sub>2026-11-19 · 4d ago</sub>

> **Feature**
> * **pptx:** Read waterfall, treemap and the other Office 2016 charts ([#5371](https://github.com/docling-project/docling/issues/5371)) ([`440492a`](https://github.com/docling-project/docling/commit/440492ac0d0e14952b32dda28fede7495611c899))
> * **email:** Add the events of calendar invitations ([#5357](https://github.com/docling-project/docling/issues/5357)) ([`6d3bb9e`](https://github.com/docling-project/docling/commit/6d3bb9ee1bffaee73f2dddfda10dc0f1c438a643))
> **Fix**
> * **pptx:** Limit the decompressed size of PPTX archive members ([#5113](https://github.com/docling-project/docling/issues/5113)) ([`587d121`](https://github.com/docling-project/docling/commit/587d12126dce2b931f105ca8c6a61cfc2b19fbf6))
> * **granite_vision:** Render table and chart crops at a configurable scale ([#5460](https://github.com/docling-project/docling/issues/5460)) ([`d1a7b7b`](https://github.com/docling-project/docling/commit/d1a7b7bfbed67d0a32e7c7a195722b6f5da20446))
> …

### [v2.150.1](https://github.com/docling-project/docling/releases/tag/v2.150.1)
<sub>2026-11-14 · 9d ago</sub>

> **Fix**
> * **cli:** Omit from_formats in convert-remote unless --from is set ([#5346](https://github.com/docling-project/docling/issues/5346)) ([`ebc50e3`](https://github.com/docling-project/docling/commit/ebc50e35057462c39771f28ca1d5c593e20a70c3))
> * **docx:** Detect headings from paragraph-level w:outlineLvl (#3312) ([#4129](https://github.com/docling-project/docling/issues/4129)) ([`31d14a7`](https://github.com/docling-project/docling/commit/31d14a74b7bddc850541ab8363b8585085845313))
> * **docx:** Keep hyperlink targets in footnotes and endnotes ([#5322](https://github.com/docling-project/docling/issues/5322)) ([`0c9a1cd`](https://github.com/docling-project/docling/commit/0c9a1cd372b49242065c7693dc0c60688733369b))
> * **docx:** Keep a single-cell table nested in a table cell inside the cell ([#5258](https://github.com/docling-project/docling/issues/5258)) ([`b9bf356`](https://github.com/docling-project/docling/commit/b9bf356f9763095ca9d51e7452a054a7db20f237))
> * **docx:** Close an open list before a table that follows it ([#5309](https://github.com/docling-project/docling/issues/5309)) ([`fec4dc3`](https://github.com/docling-project/docling/commit/fec4dc3b956db6701b7ae2bc6b28890bfd4008ee))
> …

### [v2.150.0](https://github.com/docling-project/docling/releases/tag/v2.150.0)
<sub>2026-11-10 · 13d ago</sub>

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
| 2026-11-23 | [chore: bump version to 2.152.0 [skip ci]](https://github.com/docling-project/docling/commit/311b68352d072d32831f39bd82b1804f1486e2c0) | github-actions[bot] |
| 2026-11-23 | [test: update the PowerPoint renderer dependency guard (#5540)](https://github.com/docling-project/docling/commit/07a26f2ee3c7bd978539de67b178c97a9c43d26b) | PeterStaar-IBM |
| 2026-11-23 | [feat(pdf): cancel queued PDF parsing when conversions stop (#5456)](https://github.com/docling-project/docling/commit/4c0a96de53af1032a2f2ac0375fdd7f844672349) | PeterStaar-IBM |
| 2026-11-23 | [feat(service): let the server choose the default pipeline (#4875)](https://github.com/docling-project/docling/commit/adfdff3426692a736145c3a3e0ac4fc837615d1e) | tim-roethig |
| 2026-11-23 | [fix(pdfium): keep words beside a tall cell and right-to-left runs apa…](https://github.com/docling-project/docling/commit/41dbb0c73c2c1335a0858990949501a4259619e5) | cau-git |
| 2026-11-23 | [fix(epub): find a package document stored with a literal percent sign…](https://github.com/docling-project/docling/commit/0cf0f8a1d507d5f202c5879df14337ea3bab5159) | cau-git |
| 2026-11-23 | [fix(jats): treat xref/@rid as optional and as IDREFS (#4381)](https://github.com/docling-project/docling/commit/6504fe0feef5106f35ceb72a7bd618177b08fba0) | chrikrah |
| 2026-11-23 | [fix: serialize PDFium rendering in Office backends (#5377)](https://github.com/docling-project/docling/commit/62ff440a1f0b6608a965b717c5538a8e8e034288) | xixi-box |
| 2026-11-23 | [fix(md): preserve inline HTML line breaks (#5275)](https://github.com/docling-project/docling/commit/d416bd1f78679c35321c7d008641f7f2312cd5bd) | enigma49 |
| 2026-11-23 | [fix(csv): keep fields larger than the default csv limit (#5253)](https://github.com/docling-project/docling/commit/1fb40fb41b1b980c4d0236385b06897fa2d91b60) | Viranshul-P |

[See all commits ↗](https://github.com/docling-project/docling/commits)

## ⬇️ Get it

```bash
git clone https://github.com/docling-project/docling.git
```
