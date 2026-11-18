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
| 🍴 **Forks** | 816 |
| 🐞 **Open issues + PRs** | [544](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 208.1 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.49.0rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.49.0rc0) _(pre-release)_
<sub>2026-11-16 · yesterday</sub>

> Install this pre-release version using:
> ```bash
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.49.0rc0/nvidia_modelopt-0.49.0rc0-py3-none-any.whl"
> ```

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 11d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 13d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 16d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 20d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix(config): require pydantic>=2.5.0 (#3471)](https://github.com/NVIDIA/Model-Optimizer/commit/b7f546d305d8d9800559cbc7dc86c4897f68c378) | joe-nv |
| 2026-11-18 | [docs: Link the Qwen3.8-27B draft models to their Hugging Face repos (…](https://github.com/NVIDIA/Model-Optimizer/commit/53d4eb55c0a418689e83456add1fdd8dbd14132c) | phicksy |
| 2026-11-18 | [fix(sparsity): require wonderwords>=2.2.0 (#3470)](https://github.com/NVIDIA/Model-Optimizer/commit/508e3d2cfe4102e26ac5f64c738604abe5430431) | joe-nv |
| 2026-11-18 | [Derive the GGML IQ super-block scale for local_hessian and match each…](https://github.com/NVIDIA/Model-Optimizer/commit/fe3dab761b009bea8ff3373efd6d9b5bdcbd01ca) | cjluo-nv |
| 2026-11-18 | [Fix AutoCast unknown dimension metadata (#2420)](https://github.com/NVIDIA/Model-Optimizer/commit/69dc3faa5a8162b8be1607b74bd412b339080f7b) | haoxiz-nvidia |
| 2026-11-17 | [[OMNIML-6370] [4/5] Score AutoQuantize KL candidates in a low-bit con…](https://github.com/NVIDIA/Model-Optimizer/commit/e7181568c81ff76bec7d4e420b13648451331123) | meenchen |
| 2026-11-17 | [[NVBug 6785767] Keep the RMSNorm variance in FP32 in ONNX AutoCast (#…](https://github.com/NVIDIA/Model-Optimizer/commit/8732158bb8fdb15f3c9340339434d4fe0e27f2da) | haoxiz-nvidia |
| 2026-11-17 | [Fix Qwen3.6 hybrid ONNX calibration and INT4 export (NVBug 7035423) (…](https://github.com/NVIDIA/Model-Optimizer/commit/17e646d6a7501a70793aadc1e970eadc6438ceb9) | Tracy-123-dev |
| 2026-11-17 | [[OMNIML-6104] Prepare QDQ weights during Bridge PTQ (#3366)](https://github.com/NVIDIA/Model-Optimizer/commit/5fafec084d4b01eb44927cc6cd2b0723c28e2a29) | hychiang-git |
| 2026-11-17 | [[2/2] Derive the GGML IQ super-block scales with a CUDA kernel (#3377)](https://github.com/NVIDIA/Model-Optimizer/commit/e96f81d67243c6f5cd2618e52a17abd6877d56b2) | cjluo-nv |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
