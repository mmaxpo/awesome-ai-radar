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
| 🍴 **Forks** | 829 |
| 🐞 **Open issues + PRs** | [555](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 208.0 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.49.0rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.49.0rc0) _(pre-release)_
<sub>2026-11-16 · 5d ago</sub>

> Install this pre-release version using:
> ```bash
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.49.0rc0/nvidia_modelopt-0.49.0rc0-py3-none-any.whl"
> ```

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 15d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 16d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 20d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 24d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [Add Kimi-K3.1-Pro NVFP4 recipe: recipe-driven per-module formats in t…](https://github.com/NVIDIA/Model-Optimizer/commit/3497c11ea16ff44109e8a2d581026cb1d5a7e828) | juhi10071998 |
| 2026-11-20 | [Default GPTQ to the fused NVFP4 update (#2598)](https://github.com/NVIDIA/Model-Optimizer/commit/b735732ef59c632c1d788d32e1ac024f61850016) | namgyu-yun |
| 2026-11-20 | [docs(review): check CHANGELOG entry is in the newest section (#3506)](https://github.com/NVIDIA/Model-Optimizer/commit/de3aa48ca716ff4b22d2236e1ee23dde072e32f1) | kevalmorabia97 |
| 2026-11-20 | [fix(autocast): stream calibration batches instead of materializing al…](https://github.com/NVIDIA/Model-Optimizer/commit/06d7e538158ca064d13797b94806f21f8084c144) | SID-6921 |
| 2026-11-20 | [[NVBug 7126379] Fix typos and missing words (#3501)](https://github.com/NVIDIA/Model-Optimizer/commit/9373b181766696ab5b90884c375f40b95e64911b) | noeyy-mino |
| 2026-11-20 | [MTP Boosting foundation (#3277)](https://github.com/NVIDIA/Model-Optimizer/commit/e9e80a4ef5d33dee6edd814e79ca140dbe333fdd) | talorabr |
| 2026-11-20 | [Fix quantized export state capture for FSDP2 weights (#3494)](https://github.com/NVIDIA/Model-Optimizer/commit/37da734816b7704e9dea5b81938f9ce21dd62bf6) | mxinO |
| 2026-11-19 | [Speed up GPTQ: fewer host syncs and one Hessian factorization (#3489)](https://github.com/NVIDIA/Model-Optimizer/commit/ca8e34a63c46eeaa79e23bb43359f02265346096) | cjluo-nv |
| 2026-11-19 | [Reverse the HF export's weight conversion for 3-D weights that do not…](https://github.com/NVIDIA/Model-Optimizer/commit/d2350cfcc054c98b52ff167bd8cf89f1496bdd44) | cjluo-nv |
| 2026-11-19 | [[1/3] [OMNIML-6340] Add native IQ GSQ candidates (#3287)](https://github.com/NVIDIA/Model-Optimizer/commit/4daa65defe151a0df1acb9d90a6fd9d300b391ad) | ajrasane |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
