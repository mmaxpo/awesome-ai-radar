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
| 🐞 **Open issues + PRs** | [485](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tesseract` `tesseract-ocr` `ocr` `lstm` `machine-learning` `ocr-engine` `hacktoberfest` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 54.1 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 29d ago</sub>

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

### [5.5.0](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0)
<sub>2024-11-10 · 2y ago</sub>

> **What's Changed**
> * Fix TARGET_PDB_FILE error for static linking. by @hglee in https://github.com/tesseract-ocr/tesseract/pull/4271
> * Make regular usage of CMAKE_INSTALL_LIBDIR and GNUInstallDirs by @Zopolis4 in https://github.com/tesseract-ocr/tesseract/pull/4272
> * Ignore illegal TESSDATA_PREFIX (not existing filesystem entry, issue #4277) by @stweil in https://github.com/tesseract-ocr/tesseract/pull/4278
> * Fix confidence output for the PAGE XML renderer by @JKamlah in https://github.com/tesseract-ocr/tesseract/pull/4283
> * Set hOCR capabilities ocrp_dir and ocrp_lang unconditionally by @stweil in https://github.com/tesseract-ocr/tesseract/pull/4301
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Recognize small words between lines of very large text](https://github.com/tesseract-ocr/tesseract/commit/dd8e2e48b5c0a84586e459b77321e6d1776ea5c6) | stweil |
| 2026-11-26 | [Don't clip the pixels of the image for int models](https://github.com/tesseract-ocr/tesseract/commit/4076ec73d25231be52e00c5f9a78fde2942dcb32) | stweil |
| 2026-11-26 | [Find underlined words recognized by LSTM](https://github.com/tesseract-ocr/tesseract/commit/83a92b255cdf428aaff75a872513b0502f7095fd) | stweil |
| 2026-11-26 | [Fix memory leak in MakeRowFromSubBlobs](https://github.com/tesseract-ocr/tesseract/commit/8fa860605c0e7a12775917b4d85b2125b2d0d37a) | stweil |
| 2026-11-26 | [Merge the partitions of a table in pairs](https://github.com/tesseract-ocr/tesseract/commit/5ff9208fc74491c452c0c039c4b15eeac6871b06) | stweil |
| 2026-11-26 | [Don't reject a row made from two columns as noise](https://github.com/tesseract-ocr/tesseract/commit/cc187a7e514096773790e7348fe243dc0f1a1fa1) | stweil |
| 2026-11-26 | [Find text lines which touch the edge of the image](https://github.com/tesseract-ocr/tesseract/commit/15579145177d373fac45db4b33b6feee800eb769) | stweil |
| 2026-11-26 | [Don't count leaders as image neighbours of text](https://github.com/tesseract-ocr/tesseract/commit/c90c2199d8e8f0e0b3450b56c0e67ef394787ef0) | stweil |
| 2026-11-26 | [Don't let an image take text which is not on its pixels](https://github.com/tesseract-ocr/tesseract/commit/2e47824e9122c201f2a766889e2dcbe4965058d8) | stweil |
| 2026-11-25 | [Restart rows and paragraphs from the current block](https://github.com/tesseract-ocr/tesseract/commit/3a260247375f091625378cd099713f7a4bf0e4d7) | ilkecan |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
