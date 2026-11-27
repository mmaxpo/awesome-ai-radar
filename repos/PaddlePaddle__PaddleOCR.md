# PaddlePaddle/PaddleOCR

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/PaddlePaddle/PaddleOCR)

> Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Lightweight OCR: PDFs/images to structured data |
| **Added** | 2026-11-15 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 93.4k |
| 🍴 **Forks** | 11.7k |
| 🐞 **Open issues + PRs** | [295](https://github.com/PaddlePaddle/PaddleOCR/issues) |
| 💻 **Languages** | Python 69% · C++ 11% · TypeScript 6% · Shell 5% · Swift 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ocr` `chineseocr` `pdf2markdown` `pp-ocr` `pp-structure` `document-parsing` `document-translation` `kie` `ai4science` `pdf-extractor-rag` `pdf-parser` `rag` `paddleocr-vl` |
| 🕒 **Last activity** | 2026-09-16 (2mo ago) |
| 📅 **Created** | 2020-05-08 |
| 📦 **Latest release** | [v3.7.0](https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.7.0) — 2026-06-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1924.7 MB |
| 🌐 **Website** | https://www.paddleocr.com |

## 📦 Recent releases

### [v3.7.0](https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.7.0)
<sub>2026-06-11 · 5mo ago</sub>

> **2026.6.11 v3.7.0 released**
> * **Release PP-OCRv6**
>     - **Accuracy boost**: Medium tier achieves +4.6% detection and +5.1% recognition over PP-OCRv5_server, surpassing mainstream VLMs (Qwen3-VL-235B, GPT-5.5) with only 34.5M parameters.
>     - **50 languages unified**: Single model covers Chinese, English, Japanese, and 46 Latin-script languages — no model switching needed.
>     - **Specialized scenarios**: Major improvements in digital displays, dot-matrix characters, tire prints, and industrial text recognition.
>     - **Faster inference**: 5.2× CPU speedup (OpenVINO), 6.1× on Apple M4 (tiny), 0.13s on A100 GPU.
> …

### [v3.6.0](https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.6.0)
<sub>2026-05-28 · 6mo ago</sub>

> **2026.5.28 v3.6.0 released**
> * **Release the PaddleOCR-VL-1.6 document parsing solution.**
>     - PaddleOCR-VL-1.6 is an upgraded compact document parsing model built upon PaddleOCR-VL-1.5. Through a newly introduced **region-aware data optimization framework** and a **progressive post-training recipe**, the model further enhances parsing robustness and overall recognition accuracy.
>     - PaddleOCR-VL-1.6 achieves a new state-of-the-art score of **96.33%** on the authoritative benchmark OmniDocBench v1.6, while also setting new records on OmniDocBench v1.5 and Real5-OmniDocBench. The model delivers leading performance across text, formula, and table recognition tasks, surpassing both open-source and closed-source solutions.
>     - PaddleOCR-VL-1.6 significantly improves capabilities in **table recognition**, **Chinese ancient document parsing**, and **Chinese rare character recognition**, while further enhancing performance in **seal recognition**, **text spotting**, **chart recognition**, and other diverse document scenarios.
>     - The model architecture remains fully compatible with PaddleOCR-VL-1.5, enabling **zero-cost plug-and-play migration** for existing users.
> …

### [v3.5.0](https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.5.0)
<sub>2026-04-21 · 7mo ago</sub>

> **2026.4.21 v3.5.0 released**
> * Deeply integrated with the Hugging Face ecosystem, with 20 major models supporting Transformers as the inference backend. Supports flexible switching of inference engines, including PaddlePaddle static graph, PaddlePaddle dynamic graph, or Transformers.
> * Supports conversion of common document formats (Word, Excel, Powerpoint) to Markdown.
> * The PaddleOCR-VL series, PP-StructureV3, and PP-DocTranslation support exporting parsing results to DOCX format, making it convenient to view and edit in Word.
> * Official browser inference SDK PaddleOCR.js is released, supporting running PP-OCRv5 in the browser.
> **2026.4.21 v3.5.0 发布**
> …

### [v3.4.1](https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.4.1)
<sub>2026-04-14 · 7mo ago</sub>

> **2026.4.14 v3.4.1 released**
> * PaddleOCR-VL adds `llama-cpp-server` backend support.
> * PaddleOCR-VL adds AMD GPU and Intel Arc GPU hardware support.
> * Fixed dependency issues in the PaddleOCR-VL images for Huawei NPU and KunlunXin XPU*
> * For the PaddleOCR-VL Docker Compose service, the default configuration no longer limits the maximum number of pages per request.
> **2026.4.14 v3.4.1 发布**
> …

### [v3.4.0](https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.4.0)
<sub>2026-01-29 · 10mo ago</sub>

> **2026.1.29 v3.4.0 released**
> * **Release the PaddleOCR-VL-1.5 complex document parsing solution.**
>     PaddleOCR-VL-1.5 is a new iterative version of the PaddleOCR-VL series. Based on comprehensive optimization of the core capabilities of version 1.0, the model achieves **94.5%** accuracy on the authoritative document parsing benchmark OmniDocBench v1.5, surpassing top global general-purpose large models and document parsing–specific models.
>     PaddleOCR-VL-1.5 innovatively supports **irregular-shaped bounding box localization** of document elements, enabling excellent performance in real-world application scenarios such as **scanning, skew, warping, screen-photography, and complex illumination**, achieving comprehensive SOTA performance. In addition, the model further integrates **seal recognition** and **spotting tasks**, with key metrics continuing to lead mainstream models.
>     You can use it online on the [PaddleOCR official website](https://www.paddleocr.com)﻿ or call the model API.
> * Add support for calling MLX-VLM inference services.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-09-16 | [docs: deduplicate images and streamline repository cloning (#18359)](https://github.com/PaddlePaddle/PaddleOCR/commit/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf) | cuicheng01 |
| 2026-09-16 | [docs: organize research papers and unify multilingual citations (#18357)](https://github.com/PaddlePaddle/PaddleOCR/commit/811e0c59e33c27ab0ad8c978f290b6bf534d378d) | cuicheng01 |
| 2026-07-22 | [Update README (#18272)](https://github.com/PaddlePaddle/PaddleOCR/commit/2661c7c0ef5c613e8f93c6e93b2e052399f0f854) | Bobholamovic |
| 2026-07-22 | [[Feat] Support HPD-Parsing (#18262)](https://github.com/PaddlePaddle/PaddleOCR/commit/422ce151eef0864f39774e7d2e1c7bb9d90a413d) | Bobholamovic |
| 2026-06-26 | [ci: stop using paths-ignore on required checks; short-circuit docs-on…](https://github.com/PaddlePaddle/PaddleOCR/commit/211989f046cc1878460f9e65574690c00a127a1a) | lqliu7 |
| 2026-06-25 | [fix v6 docs (#18209)](https://github.com/PaddlePaddle/PaddleOCR/commit/6d2110b743adcabe53e29b1f7af047cbc551c322) | zhangyubo0722 |
| 2026-06-22 | [docs: fix formula rendering issue and optimize ci ignore rule (#18184)](https://github.com/PaddlePaddle/PaddleOCR/commit/1af0448a200eae430b9addb40e7118d67f9840ab) | SWHL |
| 2026-06-16 | [Disable push and schedule triggers in link_check.yml](https://github.com/PaddlePaddle/PaddleOCR/commit/ef346e0b402934477489001a4d253a20dbeb72a5) | TingquanGao |
| 2026-06-12 | [add PP-OCRv6 model download links (HuggingFace & ModelScope) to all R…](https://github.com/PaddlePaddle/PaddleOCR/commit/c166448875bcecb8d3b7628fd697ac1c28f8705b) | TingquanGao |
| 2026-06-12 | [fix inference_engine doc (#18153)](https://github.com/PaddlePaddle/PaddleOCR/commit/f0bef31f676ad73b950469ebfcef1904cf07eefb) | zhang-prog |

[See all commits ↗](https://github.com/PaddlePaddle/PaddleOCR/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PaddlePaddle/PaddleOCR.git
```
