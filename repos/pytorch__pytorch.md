# pytorch/pytorch

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pytorch/pytorch)

> Tensors and Dynamic neural networks in Python with strong GPU acceleration

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | The leading deep-learning framework |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 105.8k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.7k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1699.6 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 28d ago</sub>

> **PyTorch 2.15.0 Release Notes**
> - [Highlights](#highlights)
> - [Backwards Incompatible Changes](#backwards-incompatible-changes)
> - [Deprecations](#deprecations)
> - [New Features](#new-features)
> - [Improvements](#improvements)
> …

### [v2.14.1](https://github.com/pytorch/pytorch/releases/tag/v2.14.1) — PyTorch 2.14.1 Release
<sub>2026-09-30 · 1mo ago</sub>

> This release is meant to fix the following regressions and silent correctness issues:
> **Silent correctness fixes**
> - Fix incorrect `torch.linalg.lstsq` solutions on MPS for complex batched underdetermined systems ([#196113](https://github.com/pytorch/pytorch/issues/196113)), fixed by [#196128](https://github.com/pytorch/pytorch/pull/196128)
> - Fix non-orthogonal `U` and inaccurate small singular values from `torch.linalg.svd` on MPS for rank-deficient and ill-conditioned inputs ([#196112](https://github.com/pytorch/pytorch/issues/196112)), fixed by [#196139](https://github.com/pytorch/pytorch/pull/196139) and [#199063](https://github.com/pytorch/pytorch/pull/199063)
> - Update the CUDA 13.2 Linux binaries to CUDA 13.2.2 ([#196351](https://github.com/pytorch/pytorch/pull/196351)). This NVIDIA update resolves two critical issues that could produce incorrect results ([CUDA 13.2.2 release notes](https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html#overview)):
>   - cuBLAS: `cublasLtMatmul()` could ignore tensor-wide scaling for NVFP4 matrix multiplications (introduced in CUDA 13.2 Update 1)
> …

### [v2.14.0](https://github.com/pytorch/pytorch/releases/tag/v2.14.0) — PyTorch 2.14.0 Release
<sub>2026-09-02 · 2mo ago</sub>

> **PyTorch 2.14.0 Release Notes**
> - [Highlights](#highlights)
> - [Backwards Incompatible Changes](#backwards-incompatible-changes)
> - [Deprecations](#deprecations)
> - [New Features](#new-features)
> - [Improvements](#improvements)
> …

### [v2.13.0](https://github.com/pytorch/pytorch/releases/tag/v2.13.0) — PyTorch 2.13.0 Release
<sub>2026-07-08 · 4mo ago</sub>

> **PyTorch 2.13.0 Release Notes**
> - [Highlights](#highlights)
> - [Backwards Incompatible Changes](#backwards-incompatible-changes)
> - [Deprecations](#deprecations)
> - [New Features](#new-features)
> - [Improvements](#improvements)
> …

### [v2.12.1](https://github.com/pytorch/pytorch/releases/tag/v2.12.1) — PyTorch 2.12.1 Release, bug fix release
<sub>2026-06-18 · 5mo ago</sub>

> This release is meant to fix the following regressions and silent correctness issues:
> **Regression fixes**
> - Fix nondeterministic outputs in test_batch_invariance with FLASH_ATTN on NVIDIA B200 GPUs ([#181248](https://github.com/pytorch/pytorch/issues/181248)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
> - Fix illegal memory access in the Triton convolution2d_bwd_weight kernel on B100/B200 (sm100) GPUs ([#187081](https://github.com/pytorch/pytorch/issues/187081)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
> - Fix fill_ on byte-dtype views with misaligned storage offset ([#186821](https://github.com/pytorch/pytorch/pull/186821))
> **Releng / Build**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [[optim] Validate optimizer and scheduler hyperparameters (#206075)](https://github.com/pytorch/pytorch/commit/deaabcc05036a6915e636693fa311e29b3485de8) | janeyx99 |
| 2026-11-26 | [Use torch.finfo(dtype).eps as F.normalize's default eps (#204410)](https://github.com/pytorch/pytorch/commit/30e720bcb1ae8fac699240a9627ea9d6b787fe6e) | roydonsequeira |
| 2026-11-26 | [Register hash_tensor.out for XPU backend (#204393)](https://github.com/pytorch/pytorch/commit/2e0e894eec10d73b3404acf508ae77aec9344a1a) | msnliu |
| 2026-11-26 | [Fix test ordering pollution in test_non_strict_export_distribution_va…](https://github.com/pytorch/pytorch/commit/559bef73d8a4abd8949067c50088d6b6168c84d8) | ddelgadovargas-cyber |
| 2026-11-26 | [[Testcase Refactoring] Make test_runtime_estimator.py device-generic …](https://github.com/pytorch/pytorch/commit/c83c58355eb060fcf248cae3792c2425b028fb3b) | youlituao |
| 2026-11-26 | [[Testcase Refactoring] Add HardwareClassification for shutdown_timeou…](https://github.com/pytorch/pytorch/commit/b23e4993a4471e6f251ae6706799ca90112bb9cd) | PlatformLC |
| 2026-11-26 | [Install nccl-extensions 0.2.0 in CI and load its versioned libnccl_ep…](https://github.com/pytorch/pytorch/commit/86db80054f3ebdf852fe540ef3263705443c13d2) | crcrpar |
| 2026-11-26 | [[Testcase Refactoring] Add hardware classification for test_sac_ilp.p…](https://github.com/pytorch/pytorch/commit/1a26a9151783a9087741803898a0d6a80419fb00) | kurt739910017 |
| 2026-11-26 | [[Inductor][XPU] Add persistent and non-persistent Triton mm templates…](https://github.com/pytorch/pytorch/commit/de52ac8b8b297a3d49941c8d58189ca1c46b9e16) | chunhuanMeng |
| 2026-11-26 | [[inductor] Use is_gpu for b2b_gemm device eligibility (#204568)](https://github.com/pytorch/pytorch/commit/23a4e981af806a1c582cd0e91bca063f58482db0) | SHIHAIFENG15 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
