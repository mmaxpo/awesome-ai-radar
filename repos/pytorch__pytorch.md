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
| ⭐ **Stars** | 105.7k |
| 🍴 **Forks** | 30.8k |
| 🐞 **Open issues + PRs** | [18.4k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1681.3 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 21d ago</sub>

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
| 2026-11-19 | [[CI] Run the FA3 wheel upload in a dedicated environment with approva…](https://github.com/pytorch/pytorch/commit/e4e68adf3952c9193a5a08ed97031b8769ef60c2) | atalman |
| 2026-11-19 | [[Test Refactoring] Standardizing the definition format for `device_ty…](https://github.com/pytorch/pytorch/commit/b03a81e91a34c3a95f1e47281e7bf115ba2c8c22) | fffrog |
| 2026-11-19 | [[inductor] Native matmul fixes and a hook for the Helion backend (#20…](https://github.com/pytorch/pytorch/commit/cc554b226572b6b1c2750fc845a3a6b95ad9cfab) | nullplay |
| 2026-11-19 | [[TunableOp] Close the results file when result writes stop (#202380)](https://github.com/pytorch/pytorch/commit/ec04e233cf8623c89404b947d6da3ed914c1a67b) | amd-maradosa |
| 2026-11-19 | [[distributed][Symmetric memory] Account for strides in symmetric memo…](https://github.com/pytorch/pytorch/commit/3dc057e03e29033dee100acb911cd680b980bd7b) | mansiag05 |
| 2026-11-19 | [[Inductor] Map PrivateUse1 devices to shared AOTI C++ wrapper headers…](https://github.com/pytorch/pytorch/commit/c4c9527f77b6038bbfdecf505ba19324fc80e481) | can-gaa-hou |
| 2026-11-19 | [Fix CPU separable interpolation when the output width is 1 (#204534)](https://github.com/pytorch/pytorch/commit/c3ea26b5ae46e9a9f8ac92f51ffb39a2fd88dd61) | heyludy |
| 2026-11-19 | [[profiler] Give the execution-trace pt2 tests a private inductor cach…](https://github.com/pytorch/pytorch/commit/8b97977cc95f31857c67ce324523254fffde5e39) | astachowiczhabana |
| 2026-11-19 | [[Test][XPU] Enable more `test_dataloader.py` tests on XPU (#203236)](https://github.com/pytorch/pytorch/commit/ef2846d13adb294f9229325b832affb9cdaa91f4) | pbielak |
| 2026-11-19 | [[Testcase Refactoring][PrivateUse1] Add hw_classification to test_ren…](https://github.com/pytorch/pytorch/commit/681a0229d63a9f6a613d45af02e30688fa91ab7b) | cn-sys |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
