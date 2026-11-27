# tesseract-ocr/tesseract

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/tesseract-ocr/tesseract)

> Tesseract Open Source OCR Engine (main repository)

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Classic open-source OCR engine |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 77.7k |
| 🍴 **Forks** | 10.9k |
| 🐞 **Open issues + PRs** | [486](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tesseract` `tesseract-ocr` `ocr` `lstm` `machine-learning` `ocr-engine` `hacktoberfest` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.5](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.5) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 54.4 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.5](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.5)
<sub>2026-11-26 · today</sub>

> **What's Changed**
> This release fixes nine security advisories and many crashes, endless loops and timeouts with crafted images or model files.
> Other notable changes:
> * The layout analysis finds more text: text inside a scan border, between leaders and at the edge of the image, small words between lines of very large text, and rows made from two columns.
> * PDF files get a valid ToUnicode CMap, and two cases of invalid PAGE XML output are fixed.
> * The LSTM code is faster with more SIMD functions for ARM64 and x86_64.
> …

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 1mo ago</sub>

> **What's Changed**
> This release fixes 17 security advisories and several smaller issues.
> In addition, it provides some smaller updates and improvements:
> * fix build of training tool on windows with VS2022: by @zdenop in https://github.com/tesseract-ocr/tesseract/pull/4590
> * arch,viewer: add missing <cstdlib> and <string> by @tachalorah in https://github.com/tesseract-ocr/tesseract/pull/4592
> * Fix recursive static initialization in SIMDDetect::GetDetector() by @stweil with @Copilot in https://github.com/tesseract-ocr/tesseract/pull/4598
> …

### [5.5.3](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.3)
<sub>2026-07-24 · 4mo ago</sub>

> **What's Changed**
> This release fixes two security advisories and several smaller issues.
> In addition, it provides some smaller updates and improvements:
> * Fix typos by @szepeviktor in https://github.com/tesseract-ocr/tesseract/pull/4497
> * Fix missing closing tags in multi-page PAGE XML output by @stweil with @Copilot in https://github.com/tesseract-ocr/tesseract/pull/4506
> * Fix Apple CMAKE_SYSTEM_PROCESSOR not set when crosscompiling by @ppavacic in https://github.com/tesseract-ocr/tesseract/pull/4503
> …

### [5.5.2](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.2)
<sub>2025-12-26 · 11mo ago</sub>

> **What's Changed**
> * Simplify code for osdetect by @stweil in https://github.com/tesseract-ocr/tesseract/pull/4436
> * Fix and improve configuration for cmake builds by @stweil in https://github.com/tesseract-ocr/tesseract/pull/4437
> * Modernize some for loops and fix some signed/unsigned issues by @stweil in https://github.com/tesseract-ocr/tesseract/pull/4438
> * Cmake optimization with warp2 by @zdenop in https://github.com/tesseract-ocr/tesseract/pull/4452
> * Update checkout action by @rettinghaus in https://github.com/tesseract-ocr/tesseract/pull/4461
> …

### [5.5.1](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.1)
<sub>2025-05-25 · 1y ago</sub>

> **What's Changed**
> * Fix linear congruential random number generator by @stweil in https://github.com/tesseract-ocr/tesseract/pull/4357
> * Make list classes templated by @egorpugin in https://github.com/tesseract-ocr/tesseract/pull/4356
> * add cli `-c` parameter(s) to init vectors by @zdenop in https://github.com/tesseract-ocr/tesseract/pull/4363
> * handle colormaps correctly by @zdenop in https://github.com/tesseract-ocr/tesseract/pull/4369
> * use constexpr for kDawgMagicNumber by @zdenop in https://github.com/tesseract-ocr/tesseract/pull/4378
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Create new release 5.5.5](https://github.com/tesseract-ocr/tesseract/commit/4292f6890aa86ef64eba32090358f40f69dd6d28) | stweil |
| 2026-11-26 | [ccstruct: allow MergeAdjacentBlobs for words of the LSTM recognizer](https://github.com/tesseract-ocr/tesseract/commit/51ccb12e3e469d93f036ad36c57f583c18b26273) | stweil |
| 2026-11-26 | [ccmain: do not merge the blobs of a word with a single character](https://github.com/tesseract-ocr/tesseract/commit/b2597705a281caad0a8d56a474d6ddd02b2b0bb6) | stweil |
| 2026-11-26 | [ccmain: avoid a division by zero for a page without characters](https://github.com/tesseract-ocr/tesseract/commit/3c3e087f899b1f597ef9390fd053862e5e4a905c) | stweil |
| 2026-11-26 | [ccmain: do not abort for a word with more than 512 blobs](https://github.com/tesseract-ocr/tesseract/commit/24036579bd9772458eb2b62ff4d2a53ffef0dca4) | stweil |
| 2026-11-26 | [ccmain: fix an endless loop in the fuzzy space code](https://github.com/tesseract-ocr/tesseract/commit/b998a91efc733718846137227e4cad89d21764d6) | stweil |
| 2026-11-26 | [ccmain: fix the index of the lengths in check_abbreviation](https://github.com/tesseract-ocr/tesseract/commit/feebf4e8ea666dd742383fa26ac782cb3149994b) | stweil |
| 2026-11-26 | [ccstruct: count the votes for an inverse word with int](https://github.com/tesseract-ocr/tesseract/commit/7f76d8ecbfe978c478eeae7821011c34b4e685aa) | stweil |
| 2026-11-26 | [ccstruct: allow more than 65535 characters in a REJMAP](https://github.com/tesseract-ocr/tesseract/commit/12538c836b0b6996e29b28740d894005a4d5974c) | stweil |
| 2026-11-26 | [ccmain: use int for offsets into the text of a word](https://github.com/tesseract-ocr/tesseract/commit/9085e1a321504a44248d7579d33d2ecceb2d9ff0) | stweil |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
