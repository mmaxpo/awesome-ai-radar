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
| 🍴 **Forks** | 819 |
| 🐞 **Open issues + PRs** | [551](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 214.8 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.49.0rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.49.0rc0) _(pre-release)_
<sub>2026-11-16 · 2d ago</sub>

> Install this pre-release version using:
> ```bash
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.49.0rc0/nvidia_modelopt-0.49.0rc0-py3-none-any.whl"
> ```

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 12d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 14d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 17d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 21d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Use a placeholder cluster host in the MCP README example (#3491)](https://github.com/NVIDIA/Model-Optimizer/commit/d2d92b00ed34662d835b3854bc951599a55eb760) | kevalmorabia97 |
| 2026-11-19 | [[OMNIML-6370] [5/6] Add a Qwen3.6-35B-A3B sub-4-bit AutoQuantize reci…](https://github.com/NVIDIA/Model-Optimizer/commit/17ac4fc9ad2b1b293954efa9c4bc076f803ca091) | meenchen |
| 2026-11-19 | [Apply the legacy "default" quant_cfg key first wherever it appears (#…](https://github.com/NVIDIA/Model-Optimizer/commit/a8939992aa6c781e79a739afe95ecc9104d61ada) | wguo7 |
| 2026-11-18 | [Load position ids on every PP stage when distilling VL models that us…](https://github.com/NVIDIA/Model-Optimizer/commit/c44171e85364673b776f64704356f391ee6968dd) | younes-hourri |
| 2026-11-18 | [Avoid repeated calibration inference for shared ONNX AWQ activations …](https://github.com/NVIDIA/Model-Optimizer/commit/be9c492c7422bc1a5d20d31f7cf4c2455ee146da) | Tracy-123-dev |
| 2026-11-18 | [Add per-node calibration to ONNX AutoCast (#3371)](https://github.com/NVIDIA/Model-Optimizer/commit/4579317f914083fc41dc7ff0b9bf26271ac04dc5) | gcunhase |
| 2026-11-18 | [fix(config): require pydantic>=2.5.0 (#3471)](https://github.com/NVIDIA/Model-Optimizer/commit/b7f546d305d8d9800559cbc7dc86c4897f68c378) | joe-nv |
| 2026-11-18 | [docs: Link the Qwen3.8-27B draft models to their Hugging Face repos (…](https://github.com/NVIDIA/Model-Optimizer/commit/53d4eb55c0a418689e83456add1fdd8dbd14132c) | phicksy |
| 2026-11-18 | [fix(sparsity): require wonderwords>=2.2.0 (#3470)](https://github.com/NVIDIA/Model-Optimizer/commit/508e3d2cfe4102e26ac5f64c738604abe5430431) | joe-nv |
| 2026-11-18 | [Derive the GGML IQ super-block scale for local_hessian and match each…](https://github.com/NVIDIA/Model-Optimizer/commit/fe3dab761b009bea8ff3373efd6d9b5bdcbd01ca) | cjluo-nv |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
