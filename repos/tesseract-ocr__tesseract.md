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
| ⭐ **Stars** | 77.5k |
| 🍴 **Forks** | 10.9k |
| 🐞 **Open issues + PRs** | [492](https://github.com/tesseract-ocr/tesseract/issues) |
| 💻 **Languages** | C++ 96% · CMake 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `hacktoberfest` `lstm` `machine-learning` `ocr` `ocr-engine` `tesseract` `tesseract-ocr` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2014-08-12 |
| 📦 **Latest release** | [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 53.6 MB |
| 🌐 **Website** | https://tesseract-ocr.github.io/ |

## 📦 Recent releases

### [5.5.4](https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.4)
<sub>2026-10-28 · 14d ago</sub>

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
| 2026-11-10 | [wordrec: stop the diacritics reassignment when the budget is used up](https://github.com/tesseract-ocr/tesseract/commit/4e3ec57f3039fd09e183f6884b8e1b70a57e9b0f) | stweil |
| 2026-11-10 | [wordrec: let a real result win against a fake result of an exhausted budget](https://github.com/tesseract-ocr/tesseract/commit/780f5d1a387143a1fd46de8bb2447c2cada8289b) | stweil |
| 2026-11-10 | [wordrec: do not output fake results of ambigs training](https://github.com/tesseract-ocr/tesseract/commit/5cb5ac9033e798256a6fb638520425632d4f1946) | stweil |
| 2026-11-09 | [wordrec: handle words skipped by the classification budget in more places](https://github.com/tesseract-ocr/tesseract/commit/ceb526eab6998cd292139be90f0c696df8df50f4) | stweil |
| 2026-11-06 | [wordrec: add a per-page blob classification budget to bound classifier timeouts](https://github.com/tesseract-ocr/tesseract/commit/6e5ad3d47e9a694ea6250205747ee30b6804b350) | stweil |
| 2026-11-02 | [Validate the LSTM softmax child runtime type during deserialization (#4670)](https://github.com/tesseract-ocr/tesseract/commit/c21194d06998e244754d65329d6c9f1e14fe392e) | professor-moody |
| 2026-11-02 | [Add error checking for elf_aux_info() (#4637)](https://github.com/tesseract-ocr/tesseract/commit/0860367e4ddb92df0c0d27c5c3d4100e1e385808) | brad0 |
| 2026-11-02 | [Fix exit code when no renderers could be created (#4669)](https://github.com/tesseract-ocr/tesseract/commit/4d8565029174d6d70385795eebefd876533e9b97) | VishnuSrivatsava |
| 2026-11-02 | [lstm: don't cap legitimate inference buffers in ResizeNoInit](https://github.com/tesseract-ocr/tesseract/commit/8a2cc748331b18579e763ecb9517f93a1fab803f) | stweil |
| 2026-11-02 | [Register plumbing_dimensions_test with Autotools and tidy tests](https://github.com/tesseract-ocr/tesseract/commit/70723acce95f715327189bbbfdd6172c6863f4c6) | stweil |

[See all commits ↗](https://github.com/tesseract-ocr/tesseract/commits)

## 👥 Top contributors

[stweil](https://github.com/stweil) (2545) · [zdenop](https://github.com/zdenop) (1463) · [egorpugin](https://github.com/egorpugin) (982) · [theraysmith](https://github.com/theraysmith) (565) · [amitdo](https://github.com/amitdo) (227)

## ⬇️ Get it

```bash
git clone https://github.com/tesseract-ocr/tesseract.git
```
