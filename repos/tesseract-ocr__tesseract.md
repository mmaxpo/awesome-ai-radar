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
| 🐞 **Open issues + PRs** | [490](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tesseract` `tesseract-ocr` `ocr` `lstm` `machine-learning` `ocr-engine` `hacktoberfest` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 54.1 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 28d ago</sub>

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
| 2026-11-24 | [Improve the estimation of bold for words recognized by LSTM](https://github.com/tesseract-ocr/tesseract/commit/ba7d34113947d343fd766773bb365922afda7e6e) | stweil |
| 2026-11-24 | [Estimate font styles for rotated and vertical text](https://github.com/tesseract-ocr/tesseract/commit/102fc24e8dc461a2b490f85ff0b3aab5f63da310) | stweil |
| 2026-11-24 | [Ignore specks of noise in the font style estimation](https://github.com/tesseract-ocr/tesseract/commit/d15290320d412d374914944a423c566314b6a4cf) | stweil |
| 2026-11-24 | [Estimate bold and italic for words recognized by LSTM](https://github.com/tesseract-ocr/tesseract/commit/bc852c4265edef3e6ece70266a534e06f0de4e3e) | stweil |
| 2026-11-24 | [Write font attributes in ALTO and PAGE output](https://github.com/tesseract-ocr/tesseract/commit/f4cb819ad546396a68d49a1b2ffa0eb3f74af275) | stweil |
| 2026-11-24 | [Fix crash when training continues with a new character set](https://github.com/tesseract-ocr/tesseract/commit/d16a3ecc463528f620234e2702d64963b0f1a691) | stweil |
| 2026-11-24 | [Fix IsSpaceDelimited for characters with the null script](https://github.com/tesseract-ocr/tesseract/commit/f16443b8a572c1692e4078587023d20a93cbc184) | stweil |
| 2026-11-23 | [Don't write an empty reading order in PAGE output](https://github.com/tesseract-ocr/tesseract/commit/69031805b0bf465468ead416d29753defdf397d0) | stweil |
| 2026-11-23 | [Don't write a baseline for words in PAGE output](https://github.com/tesseract-ocr/tesseract/commit/26228d001e6686bdf5cffbb420d750d186ff7d4c) | stweil |
| 2026-11-23 | [README.md: Update the 'Dependencies' section](https://github.com/tesseract-ocr/tesseract/commit/a68ecf772b265456dd04d82123ec9a7bb10aeabe) | amitdo |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
