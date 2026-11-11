# tesseract-ocr/tesseract

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/tesseract-ocr/tesseract)

> Tesseract Open Source OCR Engine (main repository)

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why I saved it** | Classic open-source OCR engine |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 77.5k |
| 🍴 **Forks** | 10.9k |
| 🐞 **Open issues + PRs** | [493](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `hacktoberfest` `lstm` `machine-learning` `ocr` `ocr-engine` `tesseract` `tesseract-ocr` |
| 🕒 **Last activity** | 2026-11-10 (today) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 53.5 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 13d ago</sub>

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
| 2026-11-02 | [Validate the LSTM softmax child runtime type during deserialization (#4670)](https://github.com/tesseract-ocr/tesseract/commit/c21194d06998e244754d65329d6c9f1e14fe392e) | professor-moody |
| 2026-11-02 | [Add error checking for elf_aux_info() (#4637)](https://github.com/tesseract-ocr/tesseract/commit/0860367e4ddb92df0c0d27c5c3d4100e1e385808) | brad0 |
| 2026-11-02 | [Fix exit code when no renderers could be created (#4669)](https://github.com/tesseract-ocr/tesseract/commit/4d8565029174d6d70385795eebefd876533e9b97) | VishnuSrivatsava |
| 2026-11-02 | [lstm: don't cap legitimate inference buffers in ResizeNoInit](https://github.com/tesseract-ocr/tesseract/commit/8a2cc748331b18579e763ecb9517f93a1fab803f) | stweil |
| 2026-11-02 | [Register plumbing_dimensions_test with Autotools and tidy tests](https://github.com/tesseract-ocr/tesseract/commit/70723acce95f715327189bbbfdd6172c6863f4c6) | stweil |
| 2026-10-28 | [Validate Plumbing child dimensions during deserialization](https://github.com/tesseract-ocr/tesseract/commit/1f7adfad28ee06afdd9d4e1b1a807c87c07c796b) | professor-moody |
| 2026-11-02 | [serialis: require declared sizes to be backed by remaining bytes (#4675)](https://github.com/tesseract-ocr/tesseract/commit/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26) | stweil |
| 2026-10-28 | [Create new release 5.5.4](https://github.com/tesseract-ocr/tesseract/commit/7e548e6eff172f38f97664afe7f7ce40db36c8d6) | stweil |
| 2026-10-27 | [Fix use-after-free in ReplaceCurrentWord with several languages (#4667)](https://github.com/tesseract-ocr/tesseract/commit/a95faa0078bcbb59357468f81e079814f8f28e74) | mardgez |
| 2026-10-27 | [Revise OS options in issue-bug.yml template](https://github.com/tesseract-ocr/tesseract/commit/a7a403c96225ee1ac2dcf43efcddf79002f14b48) | amitdo |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## 👥 Top contributors

[stweil](https://github.com/stweil) (2540) · [zdenop](https://github.com/zdenop) (1463) · [egorpugin](https://github.com/egorpugin) (982) · [theraysmith](https://github.com/theraysmith) (565) · [amitdo](https://github.com/amitdo) (227)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
