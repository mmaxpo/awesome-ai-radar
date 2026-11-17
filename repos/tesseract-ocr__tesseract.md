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
| ⭐ **Stars** | 77.6k |
| 🍴 **Forks** | 10.9k |
| 🐞 **Open issues + PRs** | [490](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tesseract` `tesseract-ocr` `ocr` `lstm` `machine-learning` `ocr-engine` `hacktoberfest` |
| 🕒 **Last activity** | 2026-11-15 (yesterday) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 53.9 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 20d ago</sub>

> **What's Changed**
> This release fixes 17 security advisories and several smaller issues.
> In addition, it provides some smaller updates and improvements:
> * fix build of training tool on windows with VS2022: by @zdenop in https://github.com/tesseract-ocr/tesseract/pull/4590
> * arch,viewer: add missing <cstdlib> and <string> by @tachalorah in https://github.com/tesseract-ocr/tesseract/pull/4592
> * Fix recursive static initialization in SIMDDetect::GetDetector() by @stweil with @Copilot in https://github.com/tesseract-ocr/tesseract/pull/4598
> …

### [5.5.3](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.3)
<sub>2026-07-24 · 3mo ago</sub>

> **What's Changed**
> This release fixes two security advisories and several smaller issues.
> In addition, it provides some smaller updates and improvements:
> * Fix typos by @szepeviktor in https://github.com/tesseract-ocr/tesseract/pull/4497
> * Fix missing closing tags in multi-page PAGE XML output by @stweil with @Copilot in https://github.com/tesseract-ocr/tesseract/pull/4506
> * Fix Apple CMAKE_SYSTEM_PROCESSOR not set when crosscompiling by @ppavacic in https://github.com/tesseract-ocr/tesseract/pull/4503
> …

### [5.5.2](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.2)
<sub>2025-12-26 · 10mo ago</sub>

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
| 2026-11-15 | [ccmain: set all results of ParagraphInfo and Orientation](https://github.com/tesseract-ocr/tesseract/commit/ddcd04239a19d3992ecc443dfa0aa025843a6614) | stweil |
| 2026-11-15 | [wordstrbox: fix missing end of the last line of a page](https://github.com/tesseract-ocr/tesseract/commit/958776bef946e65eeb41dfb8306dd29201932e9b) | stweil |
| 2026-11-15 | [hocr: escape the language name and the document title](https://github.com/tesseract-ocr/tesseract/commit/7d52a4981096140ddc9493790e23a935c458cb2f) | stweil |
| 2026-11-15 | [textord: skip the distance transform for blobs with a huge box](https://github.com/tesseract-ocr/tesseract/commit/66389e5a709f14e45cbb6191cd7e37e8d7919867) | stweil |
| 2026-11-15 | [textord: fix read out of bounds in GAPMAP for a map with one entry](https://github.com/tesseract-ocr/tesseract/commit/d41f9fee1db7a12c08208b0c4db63a6aec143060) | stweil |
| 2026-11-15 | [textord: fix loop counters and a division by zero in GAPMAP](https://github.com/tesseract-ocr/tesseract/commit/3624c6bf224719db284d97ccd3360d1e419254c0) | stweil |
| 2026-11-15 | [classify: avoid a float overflow in ReadParamDesc](https://github.com/tesseract-ocr/tesseract/commit/b31e8585de29a66e0806faae48befee283e97748) | stweil |
| 2026-11-15 | [classify: avoid linear searches by unichar id in the adaptive matcher](https://github.com/tesseract-ocr/tesseract/commit/bf506ff7daa3f0949d1a89384c4963fa6e775cd1) | stweil |
| 2026-11-15 | [cutil: fix null pointer dereference for the size of an empty LIST](https://github.com/tesseract-ocr/tesseract/commit/0d4e1a54d812c12eb39bf9d3fd886dff2e613bd0) | stweil |
| 2026-11-15 | [classify: reject an inttemp class with too many protos](https://github.com/tesseract-ocr/tesseract/commit/6b2968d65cbe62799c2ae316fc00566a07e712c6) | stweil |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
