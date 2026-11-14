# microsoft/markitdown

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/microsoft/markitdown)

> Python tool for converting files and office documents to Markdown.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Convert files and web pages to Markdown for LLMs |
| **Added** | 2026-11-14 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 195.4k |
| 🍴 **Forks** | 14.8k |
| 🐞 **Open issues + PRs** | [811](https://github.com/microsoft/markitdown/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `langchain` `openai` `autogen-extension` `autogen` `markdown` `microsoft-office` `pdf` |
| 🕒 **Last activity** | 2026-11-07 (7d ago) |
| 📅 **Created** | 2024-11-13 |
| 📦 **Latest release** | [v0.1.9](https://github.com/microsoft/markitdown/releases/tag/v0.1.9) — 2026-10-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 5.9 MB |

## 📦 Recent releases

### [v0.1.9](https://github.com/microsoft/markitdown/releases/tag/v0.1.9) — Version 0.1.9
<sub>2026-10-21 · 23d ago</sub>

> **What's Changed**
> * increase chunk size from 512 bytes to 64 KB for HTTP response reading by @YasirAlibrahem in https://github.com/microsoft/markitdown/pull/1511
> * fix(wikipedia): accept mobile (m.wikipedia.org) URLs by @GopalGB in https://github.com/microsoft/markitdown/pull/1850
> * fix: handle None sys.stdout.encoding in CLI output by @octo-patch in https://github.com/microsoft/markitdown/pull/1656
> * Add language parameter for the audio transcription by @hchmch in https://github.com/microsoft/markitdown/pull/1295
> * Perf: Optimize non-seekable stream buffering using shutil.copyfileobj by @YasirAlibrahem in https://github.com/microsoft/markitdown/pull/1510
> …

### [v0.1.8](https://github.com/microsoft/markitdown/releases/tag/v0.1.8) — Version 0.1.8
<sub>2026-09-21 · 1mo ago</sub>

> This release rolls up dozens of small patches and bug fixes. For typical inputs and use cases, we expect outputs and behavior to remain largely unchanged from version 0.1.7.
> The markitdown-ocr plugin has also been refactored to simplify future maintenance.
> -----
> **What's Changed**
> * Mitigate UnicodeDecodeError due to wrong ASCII charset guess for long files by @fcatalan92 in https://github.com/microsoft/markitdown/pull/2360
> * fix: support extended content-disposition filenames by @cat0825 in https://github.com/microsoft/markitdown/pull/2045
> …

### [v0.1.8b2](https://github.com/microsoft/markitdown/releases/tag/v0.1.8b2) — Version 0.1.8b2 _(pre-release)_
<sub>2026-09-14 · 2mo ago</sub>

> **What's Changed**
> * Pin GitHub Actions to full-length commit SHAs by @danfiedler-msft in https://github.com/microsoft/markitdown/pull/2316
> * Mitigate UnicodeDecodeError due to wrong ASCII charset guess for long files by @fcatalan92 in https://github.com/microsoft/markitdown/pull/2360
> * fix: support extended content-disposition filenames by @cat0825 in https://github.com/microsoft/markitdown/pull/2045
> * fix: fall back to plain text when RSS item content triggers RecursionError by @shoemoney in https://github.com/microsoft/markitdown/pull/2333
> * fix(cli): allow Content Understanding conversion from stdin by @uczltw6 in https://github.com/microsoft/markitdown/pull/2318
> …

### [v0.1.8b1](https://github.com/microsoft/markitdown/releases/tag/v0.1.8b1) — Version 0.1.8b1 _(pre-release)_
<sub>2026-09-04 · 2mo ago</sub>

> This prerelease includes numerous small bug fixes. None adds new features or is expected to change output in typical cases. Nevertheless, the volume of changes warrants a cautious rollout.
> Please report any issues or regressions.
> **What's Changed**
> * Pin GitHub Actions to full-length commit SHAs by @danfiedler-msft in https://github.com/microsoft/markitdown/pull/2316
> * Mitigate UnicodeDecodeError due to wrong ASCII charset guess for long files by @fcatalan92 in https://github.com/microsoft/markitdown/pull/2360
> * fix: support extended content-disposition filenames by @cat0825 in https://github.com/microsoft/markitdown/pull/2045
> …

### [v0.1.7](https://github.com/microsoft/markitdown/releases/tag/v0.1.7) — Version 0.1.7
<sub>2026-07-29 · 3mo ago</sub>

> **What's Changed**
> * fix: avoid O(n^2) value lookups in PPTX chart conversion by @kz-000 in https://github.com/microsoft/markitdown/pull/2227
> * Fix invalid LaTeX macros for mu, nu, tau, and down-arrow in equation conversion by @ksprajapatii in https://github.com/microsoft/markitdown/pull/2228
> * Fix typos and formatting in comments, docstrings, and markdown by @chienyuanchang in https://github.com/microsoft/markitdown/pull/2223
> * fix: handle PPTX SVG images without a rasterized fallback by @guoyu-wang in https://github.com/microsoft/markitdown/pull/2233
> * Fix omml template bugs. by @afourney in https://github.com/microsoft/markitdown/pull/2257
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-07 | [fix: match ExifTool directories case-insensitively on Windows (#2837)](https://github.com/microsoft/markitdown/commit/ed178952a6672abdfd35b5f9e76a80b6cefc086e) | Yasser-Ameur |
| 2026-11-06 | [Override default SpeechRecognition endpoint (#2846)](https://github.com/microsoft/markitdown/commit/3ae4f03dd6a7fbf0420e0f29393f175e72f123fd) | afourney |
| 2026-11-06 | [Clarify hosted service requirements in README (#2845)](https://github.com/microsoft/markitdown/commit/1dccd8318c87c4ac9f1595102b3c11e53f6f8105) | afourney |
| 2026-10-22 | [feat(doc-intel): expose models, features, query fields, and structure…](https://github.com/microsoft/markitdown/commit/7482c092d9c0074a89803c9fdb63a969e7fe17fc) | chienyuanchang |
| 2026-10-21 | [Bump versions, prior to point-release. (#2733)](https://github.com/microsoft/markitdown/commit/21d9c1d01ecc12538dab19811fd247ef2f96ef60) | afourney |
| 2026-10-21 | [Update Black, Pillow, and Windows ARM Cryptography baselines (#2731)](https://github.com/microsoft/markitdown/commit/3cf47504c5d372a65f821a04ef1809a42f27d69c) | afourney |
| 2026-10-21 | [Require certifi>=2026.10.19 for updated CA trust (#2730)](https://github.com/microsoft/markitdown/commit/f9affc86ea7cc1be2e8dd03c0e78cfcd5ae6ba64) | afourney |
| 2026-10-21 | [Bump Mammoth dependency to >=1.12.2,<2 (#2729)](https://github.com/microsoft/markitdown/commit/c907c4cd9da133e5fbe223160181524e40c8b699) | afourney |
| 2026-10-20 | [Bump the magika dependency (#2722)](https://github.com/microsoft/markitdown/commit/69e208746aa5804087e9984d585eab21667e9b0f) | afourney |
| 2026-10-04 | [Restore JSON regression coverage for late non-ASCII text (#2601)](https://github.com/microsoft/markitdown/commit/4cc9fa17653d695d64fb9eee5b33d4de55ff84e8) | afourney |

[See all commits ↗](https://github.com/microsoft/markitdown/commits)

## ⬇️ Get it

```bash
git clone https://github.com/microsoft/markitdown.git
```
