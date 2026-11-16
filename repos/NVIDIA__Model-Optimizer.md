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
| ⭐ **Stars** | 5.6k |
| 🍴 **Forks** | 809 |
| 🐞 **Open issues + PRs** | [529](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 194.3 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 9d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 10d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 14d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 18d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

### [0.48.0rc1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc1) _(pre-release)_
<sub>2026-10-17 · 29d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc1/nvidia_modelopt-0.48.0rc1-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [Prepare reproducible chat blends with question-isolated splits (#3160)](https://github.com/NVIDIA/Model-Optimizer/commit/6c85409916c66e778c4569b17efca9de577622da) | yueshen2016 |
| 2026-11-15 | [fix(speculative): one label alignment per projector_type; DSpark and …](https://github.com/NVIDIA/Model-Optimizer/commit/9047bbd418aaeeaf251fc286d2c3e8ac04bee29f) | h-guo18 |
| 2026-11-15 | [Load nested Nemotron final norms during draft training (#3275)](https://github.com/NVIDIA/Model-Optimizer/commit/d9ff11fb8d000eaa8b5bfad4c51c49f8dfc6031d) | sragrawal |
| 2026-11-13 | [[6437794] Fix ONNX autotune verbose logging (#3382)](https://github.com/NVIDIA/Model-Optimizer/commit/ef893e77084198c161cc908eb91380b3a47eccad) | gcunhase |
| 2026-11-13 | [Expose the remote AutoTune engine path (#3379)](https://github.com/NVIDIA/Model-Optimizer/commit/e169b4c2bc62a32c45aaef793cde7599dee2c1b2) | gcunhase |
| 2026-11-13 | [fix: make huggingface_hub plugin import optional (#2250)](https://github.com/NVIDIA/Model-Optimizer/commit/cc6963dea0a6f01d90d66c7699baf3884df5f64a) | Y-T-G |
| 2026-11-13 | [Preserve conversation and template inputs in streaming datasets (#3231)](https://github.com/NVIDIA/Model-Optimizer/commit/f7beef20efe2f50af93777b29cb2bd3f0286e1a6) | sragrawal |
| 2026-11-13 | [Fix EAGLE3 training input normalization (#3228)](https://github.com/NVIDIA/Model-Optimizer/commit/9002cb3b58432f6c25e9c53553c902ccf292db05) | sragrawal |
| 2026-11-13 | [Add experimental NVFP4 QAD adapter for NeMo AutoModel experts (#3164)](https://github.com/NVIDIA/Model-Optimizer/commit/1318c296fca258880834d159c98bc01ff45f1776) | Edwardf0t1 |
| 2026-11-13 | [[OMNIML-6370] [3/5] Finalize AutoQuantize selections with sequential …](https://github.com/NVIDIA/Model-Optimizer/commit/9dc922121835c489615240ef60ba8f753efa630e) | meenchen |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
