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
| 🍴 **Forks** | 813 |
| 🐞 **Open issues + PRs** | [534](https://github.com/NVIDIA/Model-Optimizer/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2024-04-23 |
| 📦 **Latest release** | [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 190.5 MB |
| 🌐 **Website** | https://nvidia.github.io/Model-Optimizer/ |

## 📦 Recent releases

### [0.49.0rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.49.0rc0) _(pre-release)_
<sub>2026-11-16 · today</sub>

> Install this pre-release version using:
> ```bash
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.49.0rc0/nvidia_modelopt-0.49.0rc0-py3-none-any.whl"
> ```

### [0.47.1](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1) — ModelOpt 0.47.1 Release
<sub>2026-11-06 · 10d ago</sub>

> **Bug Fixes**
> - Fix NVFP4 fake quantization (e.g. ``NVFP4_DEFAULT_CFG``) with Triton 3.9, as in the PyTorch 26.11 container, on GPUs with compute capability 8.9 or newer: it failed with ``NotImplementedError: Block pointers have been removed in favor of the tensor descriptor API``.

### [0.47.1rc0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.1rc0) _(pre-release)_
<sub>2026-11-05 · 12d ago</sub>

> -

### [0.48.0](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0) — ModelOpt 0.48.0 Release
<sub>2026-11-02 · 15d ago</sub>

> **New Features**
> **Sparsity**
> - Add skip-softmax calibration through vLLM for FlashAttention and FlashInfer, requiring `--validation_prompts_file` and validating serving sparsity on calibration and held-out prompts before exporting prefill/decode fits and their validation scope as `sparse_attention_config`. Calibration uses single-sequence, unchunked eager execution; serving preserves the calibrated 128-token KV-tile granularity and 128-row prefill Q tiles, autotunes only its execution schedule, and uses a smaller Q tile for one-token decode.
> - Sparse-only vLLM installs now reject unsupported DCP, DBO/ubatching, speculative decoding, and FULL mixed-batch CUDA graphs; calibrated decode also rejects FULL decode graphs.
> **Quantization**
> - Add metadata-only export specifications and non-mutating per-weight quantizer-state capture.
> …

### [0.48.0rc2](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.48.0rc2) _(pre-release)_
<sub>2026-10-28 · 19d ago</sub>

> Install this pre-release version using:
> ```
> pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.48.0rc2/nvidia_modelopt-0.48.0rc2-py3-none-any.whl"
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(onnx): require onnxslim 0.1.78 for ONNX 1.21 (#3414)](https://github.com/NVIDIA/Model-Optimizer/commit/a35496172d843be51292af82497ab5b0727f2af2) | kevalmorabia97 |
| 2026-11-17 | [[NVBug 6968503] Add axis/block_size to INT4 RTN Q/DQ nodes (#3126)](https://github.com/NVIDIA/Model-Optimizer/commit/af54ce4addb2558221823111bf14de705b9a91a9) | haoxiz-nvidia |
| 2026-11-17 | [Derive the GGML IQ super-block scale and match each block's output en…](https://github.com/NVIDIA/Model-Optimizer/commit/b1f5540c46653082ee28a553096668cde87b9816) | cjluo-nv |
| 2026-11-17 | [Ask agents for problem-first PR descriptions with a modules-touched s…](https://github.com/NVIDIA/Model-Optimizer/commit/ee4782b717450f04c3dcfe7616cbc4c1ed8e38ce) | cjluo-nv |
| 2026-11-17 | [Fix BF16 FP8 ONNX export with ml_dtypes 0.7.0 (#3405)](https://github.com/NVIDIA/Model-Optimizer/commit/e03b63b27c2a94701e125c429707cc0101aaa5bb) | ajrasane |
| 2026-11-16 | [[3/5] Move skill evaluation datasets to canonical paths (#3374)](https://github.com/NVIDIA/Model-Optimizer/commit/0bf5f4310e0a698ebb514ba336fbdd9610cbeece) | chadvoegele |
| 2026-11-16 | [Fix nightly: test_qad multi-GPU check and speculative SP gradient tes…](https://github.com/NVIDIA/Model-Optimizer/commit/e5cce4924f267d6862ded146aa243b53bc8c5cfe) | kevalmorabia97 |
| 2026-11-16 | [Fix NaN amax when restoring a quantized Megatron-Core model before it…](https://github.com/NVIDIA/Model-Optimizer/commit/6f4cb4a82caf4ff8b7edb78d5ef597b286e2c8a7) | kevalmorabia97 |
| 2026-11-16 | [docs: split changelog sections to reduce merge conflicts; add 0.50 se…](https://github.com/NVIDIA/Model-Optimizer/commit/b42551b0e3451a8cba51e67eddc260436d96bc7f) | kevalmorabia97 |
| 2026-11-16 | [[chore]: weekly bump of uv.lock on main (2026-11-16) (#3395)](https://github.com/NVIDIA/Model-Optimizer/commit/5119f8c36fa730d7f7c7d38a082b8be5ed02043c) | github-actions[bot] |

[See all commits ↗](https://github.com/NVIDIA/Model-Optimizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NVIDIA/Model-Optimizer.git
```
