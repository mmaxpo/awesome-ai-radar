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
| 🍴 **Forks** | 835 |
| 🐞 **Open issues + PRs** | [595](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 219.5 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.49.0rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.49.0rc0) _(pre-release)_
<sub>2026-11-16 · 9d ago</sub>

> Install this pre-release version using:
> ```bash
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.49.0rc0/nvidia_modelopt-0.49.0rc0-py3-none-any.whl"
> ```

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 19d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 21d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 24d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 28d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [[2/2] refactor(speculative): train DSpark and Domino through the shar…](https://github.com/NVIDIA/Model-Optimizer/commit/49e04f77434d35489550c3098d69074c059eb428) | h-guo18 |
| 2026-11-25 | [Fix FSDP2 load of Qwen3.5 VLM checkpoints on Transformers 5.5 (#3559)](https://github.com/NVIDIA/Model-Optimizer/commit/f8597abcde0f1ececa76aa41c1721f0abbc05188) | sugunav14 |
| 2026-11-25 | [[NVBug 7128605] Add an opt-in W4A8 AWQ recipe for dense Qwen3.5 on Te…](https://github.com/NVIDIA/Model-Optimizer/commit/10a884d8fe0fbf1c21326fab205b3b61d3c02623) | meenchen |
| 2026-11-25 | [[NVBug 7042245] Revert only the conversions a load used on transforme…](https://github.com/NVIDIA/Model-Optimizer/commit/719cb39fbcf0d2035b38763be9a4a364744e9c09) | sugunav14 |
| 2026-11-25 | [[1/2] refactor(speculative): hand the DFlash-family loss one context …](https://github.com/NVIDIA/Model-Optimizer/commit/27a504479bc0a615fadade6e8a9759041d778f0b) | h-guo18 |
| 2026-11-25 | [Fix save_pretrained for Hugging Face MoE models with quantized fused …](https://github.com/NVIDIA/Model-Optimizer/commit/a6d3d73ef357676138010bd1f2913e23f4680d48) | sychen52 |
| 2026-11-24 | [skills: move the generic launcher guide to the common skill (#3500)](https://github.com/NVIDIA/Model-Optimizer/commit/d69d66eb989869402b1a605f9d6879c75f462cef) | Zhehao-Hu |
| 2026-11-24 | [Keep the source checkpoint's layer_types in the exported config (#3558)](https://github.com/NVIDIA/Model-Optimizer/commit/8a79310a9630bfd245c7ea032f786948e4a51f6b) | Fridah-nv |
| 2026-11-24 | [[OMNIML-6062] Dequantize block-FP8 weights that load in the model dty…](https://github.com/NVIDIA/Model-Optimizer/commit/16af4b9c54214e58fe6fac95a66c58c43c4bcea3) | shengliangxu |
| 2026-11-24 | [[OMNIML-6624] Fix KV-cache growth during layerwise GPTQ calibration (…](https://github.com/NVIDIA/Model-Optimizer/commit/c6345c549af0358156f726bce7c0679969d7f17c) | meenchen |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
