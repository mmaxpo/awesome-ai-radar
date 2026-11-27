# NVIDIA/Model-Optimizer

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/NVIDIA/Model-Optimizer)

> A unified library of SOTA model optimization techniques like quantization, distillation, pruning, neural architecture search, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Quantize and optimize models for local hardware |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 5.7k |
| 🍴 **Forks** | 839 |
| 🐞 **Open issues + PRs** | [603](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 217.5 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.49.0rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.49.0rc0) _(pre-release)_
<sub>2026-11-16 · 10d ago</sub>

> Install this pre-release version using:
> ```bash
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.49.0rc0/nvidia_modelopt-0.49.0rc0-py3-none-any.whl"
> ```

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 20d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 22d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 25d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 29d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [Improve the TensorRT custom-layer introspection diagnostic (#2734)](https://github.com/NVIDIA/Model-Optimizer/commit/d6b941ee97d3277fd957c0e092a0c55ecfd66ff0) | v0ropaev |
| 2026-11-26 | [[OMNIML-5967] [1/6] Preserve buffer persistence through Accelerate of…](https://github.com/NVIDIA/Model-Optimizer/commit/ba1366ec59052cbf03d57fea58060ef4df4e0695) | Separius |
| 2026-11-26 | [Fix ONNX AWQ-Lite get_weight_scale mixing rows from different blocks …](https://github.com/NVIDIA/Model-Optimizer/commit/6838419c83471fad1a51ffe28f57df45d0af27d1) | SID-6921 |
| 2026-11-26 | [Do not leave 'trt' in the autocast providers default after one conver…](https://github.com/NVIDIA/Model-Optimizer/commit/c7cc60801bbbb62f3a7f00b5be8ce6b6596b2d95) | v0ropaev |
| 2026-11-26 | [[2/2] refactor(speculative): train DSpark and Domino through the shar…](https://github.com/NVIDIA/Model-Optimizer/commit/49e04f77434d35489550c3098d69074c059eb428) | h-guo18 |
| 2026-11-25 | [Fix FSDP2 load of Qwen3.5 VLM checkpoints on Transformers 5.5 (#3559)](https://github.com/NVIDIA/Model-Optimizer/commit/f8597abcde0f1ececa76aa41c1721f0abbc05188) | sugunav14 |
| 2026-11-25 | [[NVBug 7128605] Add an opt-in W4A8 AWQ recipe for dense Qwen3.5 on Te…](https://github.com/NVIDIA/Model-Optimizer/commit/10a884d8fe0fbf1c21326fab205b3b61d3c02623) | meenchen |
| 2026-11-25 | [[NVBug 7042245] Revert only the conversions a load used on transforme…](https://github.com/NVIDIA/Model-Optimizer/commit/719cb39fbcf0d2035b38763be9a4a364744e9c09) | sugunav14 |
| 2026-11-25 | [[1/2] refactor(speculative): hand the DFlash-family loss one context …](https://github.com/NVIDIA/Model-Optimizer/commit/27a504479bc0a615fadade6e8a9759041d778f0b) | h-guo18 |
| 2026-11-25 | [Fix save_pretrained for Hugging Face MoE models with quantized fused …](https://github.com/NVIDIA/Model-Optimizer/commit/a6d3d73ef357676138010bd1f2913e23f4680d48) | sychen52 |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
