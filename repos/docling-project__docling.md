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
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2024-07-09 |
| 📦 **Latest release** | [v2.151.1](https://github.com/docling-project/docling/releases/tag/v2.151.1) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 473.4 MB |
| 🌐 **Website** | https://docling-project.github.io/docling |

## 📦 Recent releases

### [v2.151.1](https://github.com/docling-project/docling/releases/tag/v2.151.1)
<sub>2026-11-19 · 2d ago</sub>

> **Fix**
> * **service-client:** Keep the WebSocket poll fallback within the original timeout ([#5121](https://github.com/docling-project/docling/issues/5121)) ([`f9249e5`](https://github.com/docling-project/docling/commit/f9249e5067d7dacc01bd9a55abf5eb945b3861d0))
> * **service-client:** Propagate input iterator errors ([#5013](https://github.com/docling-project/docling/issues/5013)) ([`1150323`](https://github.com/docling-project/docling/commit/11503233cc174f6f7eedc32e2f03c46a93c69176))
> * Preserve VLM page-range provenance and verify complete assembly ([#4498](https://github.com/docling-project/docling/issues/4498)) ([`5068b03`](https://github.com/docling-project/docling/commit/5068b0365c347641fe51219dd9b754357aa32c93))
> * Avoid OpenCV FIPS aborts with Databricks opt-out setting ([#5430](https://github.com/docling-project/docling/issues/5430)) ([`de09f2a`](https://github.com/docling-project/docling/commit/de09f2a81460fb8439fc228d09d0faeeec48d301))
> * **docx:** Keep XML comments in NOTES, drop processing instructions ([#4584](https://github.com/docling-project/docling/issues/4584)) ([`f13a8bc`](https://github.com/docling-project/docling/commit/f13a8bc98532abcd7b306fd83d6486bc9afcddc2))
> …

### [v2.151.0](https://github.com/docling-project/docling/releases/tag/v2.151.0)
<sub>2026-11-19 · 3d ago</sub>

> **Feature**
> * **pptx:** Read waterfall, treemap and the other Office 2016 charts ([#5371](https://github.com/docling-project/docling/issues/5371)) ([`440492a`](https://github.com/docling-project/docling/commit/440492ac0d0e14952b32dda28fede7495611c899))
> * **email:** Add the events of calendar invitations ([#5357](https://github.com/docling-project/docling/issues/5357)) ([`6d3bb9e`](https://github.com/docling-project/docling/commit/6d3bb9ee1bffaee73f2dddfda10dc0f1c438a643))
> **Fix**
> * **pptx:** Limit the decompressed size of PPTX archive members ([#5113](https://github.com/docling-project/docling/issues/5113)) ([`587d121`](https://github.com/docling-project/docling/commit/587d12126dce2b931f105ca8c6a61cfc2b19fbf6))
> * **granite_vision:** Render table and chart crops at a configurable scale ([#5460](https://github.com/docling-project/docling/issues/5460)) ([`d1a7b7b`](https://github.com/docling-project/docling/commit/d1a7b7bfbed67d0a32e7c7a195722b6f5da20446))
> …

### [v2.150.1](https://github.com/docling-project/docling/releases/tag/v2.150.1)
<sub>2026-11-14 · 8d ago</sub>

> **Fix**
> * **cli:** Omit from_formats in convert-remote unless --from is set ([#5346](https://github.com/docling-project/docling/issues/5346)) ([`ebc50e3`](https://github.com/docling-project/docling/commit/ebc50e35057462c39771f28ca1d5c593e20a70c3))
> * **docx:** Detect headings from paragraph-level w:outlineLvl (#3312) ([#4129](https://github.com/docling-project/docling/issues/4129)) ([`31d14a7`](https://github.com/docling-project/docling/commit/31d14a74b7bddc850541ab8363b8585085845313))
> * **docx:** Keep hyperlink targets in footnotes and endnotes ([#5322](https://github.com/docling-project/docling/issues/5322)) ([`0c9a1cd`](https://github.com/docling-project/docling/commit/0c9a1cd372b49242065c7693dc0c60688733369b))
> * **docx:** Keep a single-cell table nested in a table cell inside the cell ([#5258](https://github.com/docling-project/docling/issues/5258)) ([`b9bf356`](https://github.com/docling-project/docling/commit/b9bf356f9763095ca9d51e7452a054a7db20f237))
> * **docx:** Close an open list before a table that follows it ([#5309](https://github.com/docling-project/docling/issues/5309)) ([`fec4dc3`](https://github.com/docling-project/docling/commit/fec4dc3b956db6701b7ae2bc6b28890bfd4008ee))
> …

### [v2.150.0](https://github.com/docling-project/docling/releases/tag/v2.150.0)
<sub>2026-11-10 · 12d ago</sub>

> **Feature**
> * **xbrl:** Support iXBRL input and remote taxonomy resolution with source_uri ([#4689](https://github.com/docling-project/docling/issues/4689)) ([`43c016c`](https://github.com/docling-project/docling/commit/43c016caedf076b3016fe6cdd4ec4d2b53b5acc1))
> **Fix**
> * **email:** Preserve furniture from HTML message bodies ([#5228](https://github.com/docling-project/docling/issues/5228)) ([`75a7dbc`](https://github.com/docling-project/docling/commit/75a7dbc75caadddbdb1c283c8141fb1857ff8bc6))
> * **odf:** Show the displayed text of typed table cells ([#5232](https://github.com/docling-project/docling/issues/5232)) ([`b92f77c`](https://github.com/docling-project/docling/commit/b92f77cfcddd31ad5d849d9eef02072b43c51d45))
> * **example:** Avoid exposing original PII by default ([#5182](https://github.com/docling-project/docling/issues/5182)) ([`e77fcc2`](https://github.com/docling-project/docling/commit/e77fcc22863cca3097a1cb20c0496e83ef831c18))
> …

### [v2.149.0](https://github.com/docling-project/docling/releases/tag/v2.149.0)
<sub>2026-11-08 · 14d ago</sub>

> **Feature**
> * **pdf:** Add opt-in embedded PDF image extraction ([#5143](https://github.com/docling-project/docling/issues/5143)) ([`3df6c93`](https://github.com/docling-project/docling/commit/3df6c9318fc6d91fde424c90a28fc7d7e5f080dc))
> * Refactored the cli to be more intuitive ([#5214](https://github.com/docling-project/docling/issues/5214)) ([`55f21d6`](https://github.com/docling-project/docling/commit/55f21d6a439a236965542f4fd2f21d8366306b93))
> * **asr:** Add support for mlx-audio ([#5181](https://github.com/docling-project/docling/issues/5181)) ([`756059c`](https://github.com/docling-project/docling/commit/756059c2666753890e3f531ff5d6416be8b3df0e))
> * **vlm:** Add MiniCPM-OCR preset ([#5134](https://github.com/docling-project/docling/issues/5134)) ([`1282e3d`](https://github.com/docling-project/docling/commit/1282e3d9fa34f28772785177f1f330936e8df96a))
> **Fix**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [fix(email): handle UnicodeDecodeError for .msg files with 8-bit body …](https://github.com/docling-project/docling/commit/0f3564c772e006c73417f61658a2d41c8352224d) | todkarsant |
| 2026-11-20 | [feat: turn audio/video transcripts and slide media into tracks (#4752)](https://github.com/docling-project/docling/commit/5182e556308958f3ac4762bb7d03a092c2f339c9) | DanielNg0729 |
| 2026-11-20 | [fix(calendar): describe expanded days of monthly and yearly rules as …](https://github.com/docling-project/docling/commit/f93ee6bc72717da7384389434d90fbb1977047df) | gagan-baghel |
| 2026-11-20 | [docs(examples): pass engine_type to ApiVlmEngineOptions (#5380)](https://github.com/docling-project/docling/commit/77907bbe40d0dc62436bae078ebb6ec7d772e396) | usercjr |
| 2026-11-20 | [feat(heading-hierarchy): read keyword markers of other languages (#5474)](https://github.com/docling-project/docling/commit/557df045572672b4cf62a119c5252af49938a10b) | DanielNg0729 |
| 2026-11-19 | [feat(vlm): add native MLX support for Nemotron 3.5 Parse (#4934)](https://github.com/docling-project/docling/commit/825c77458b4d05ed7071d0789dc8e40ba9d18211) | geoHeil |
| 2026-11-19 | [chore: bump version to 2.151.1 [skip ci]](https://github.com/docling-project/docling/commit/56d39ffe214f59299963ed0ffb14ae29540bea99) | github-actions[bot] |
| 2026-11-19 | [fix(service-client): keep the WebSocket poll fallback within the orig…](https://github.com/docling-project/docling/commit/f9249e5067d7dacc01bd9a55abf5eb945b3861d0) | TemitopeKadri |
| 2026-11-19 | [fix(service-client): propagate input iterator errors (#5013)](https://github.com/docling-project/docling/commit/11503233cc174f6f7eedc32e2f03c46a93c69176) | Gout999 |
| 2026-11-19 | [fix: preserve VLM page-range provenance and verify complete assembly …](https://github.com/docling-project/docling/commit/5068b0365c347641fe51219dd9b754357aa32c93) | geoHeil |

[See all commits ↗](https://github.com/docling-project/docling/commits)

## ⬇️ Get it

```bash
git clone https://github.com/docling-project/docling.git
```
