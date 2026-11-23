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
| 🐞 **Open issues + PRs** | [492](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tesseract` `tesseract-ocr` `ocr` `lstm` `machine-learning` `ocr-engine` `hacktoberfest` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 54.0 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 26d ago</sub>

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
| 2026-11-23 | [Don't write an empty reading order in PAGE output](https://github.com/tesseract-ocr/tesseract/commit/69031805b0bf465468ead416d29753defdf397d0) | stweil |
| 2026-11-23 | [Don't write a baseline for words in PAGE output](https://github.com/tesseract-ocr/tesseract/commit/26228d001e6686bdf5cffbb420d750d186ff7d4c) | stweil |
| 2026-11-23 | [README.md: Update the 'Dependencies' section](https://github.com/tesseract-ocr/tesseract/commit/a68ecf772b265456dd04d82123ec9a7bb10aeabe) | amitdo |
| 2026-11-20 | [classify: limit Min and Max instead of the range in ReadParamDesc](https://github.com/tesseract-ocr/tesseract/commit/2516f31c560e056449b6d9e95e10c6feeb6ad618) | stweil |
| 2026-11-19 | [fix: link the autotools shared library to Accelerate (#4636)](https://github.com/tesseract-ocr/tesseract/commit/9c1f34d35195c8a7dae843b906924bb3f5b8b9f2) | mvanhorn |
| 2026-11-19 | [Fix crashes in the result iterators for words without best_choice (#4…](https://github.com/tesseract-ocr/tesseract/commit/1e2735f2681503a38388841aa1d6f6071aeb0ff6) | zdenop |
| 2026-11-18 | [Fix unresolved merge conflict in Makefile.am](https://github.com/tesseract-ocr/tesseract/commit/0c7dc2f312e12c6dd1efceff5d82fa01106446bb) | stweil |
| 2026-11-18 | [benchmark: add clang-22 results and a summary over all platforms](https://github.com/tesseract-ocr/tesseract/commit/ceef685ab51e4b73df4bdcbd09e26dd9a33f1ca9) | stweil |
| 2026-11-18 | [lstm: use NEON for tanh, the logistic function and the conversion to …](https://github.com/tesseract-ocr/tesseract/commit/993de3d7f26b9963e237ef8680621e8d5a1563d0) | stweil |
| 2026-11-18 | [benchmark: add results for an AMD EPYC 9554](https://github.com/tesseract-ocr/tesseract/commit/b07e3488ad16e1dc78c1f96f016a2bd315fd4b5a) | stweil |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
