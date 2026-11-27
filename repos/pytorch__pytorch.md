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
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1695.9 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 29d ago</sub>

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
| 2026-11-27 | [[inductor] Bind base shape symbols when decomposing scan/map to while…](https://github.com/pytorch/pytorch/commit/58c7687e2fc0e919f1fcc5ec5989ed4b32ed845a) | bohnstingl |
| 2026-11-27 | [Implement histogram meta functions. (#202037)](https://github.com/pytorch/pytorch/commit/7a74b6d8fb1d1fdf13660a30237063ae65279bd1) | AKloniecki |
| 2026-11-27 | [Fix linalg.eig/eigvals mutating column-major CUDA inputs (#206233)](https://github.com/pytorch/pytorch/commit/8ea8a4a1a89e0bb71102110591c070ac6f944611) | johannesz-codes |
| 2026-11-27 | [[Testcase Refactoring] 1. Add instantiate_device_type_tests to genera…](https://github.com/pytorch/pytorch/commit/7cd8428b4037ee46d80d98f6305fc85ddbb3b757) | wyb2939 |
| 2026-11-27 | [Register narrow_copy.out on XPU. (#202200)](https://github.com/pytorch/pytorch/commit/9f04cce79d76fae62123d0fba11a9e1fccebbc0c) | AKloniecki |
| 2026-11-27 | [[XPU][Profiler][UT]Enable TestProfilerEventsParityDevice and TestProf…](https://github.com/pytorch/pytorch/commit/e63b4feb0719ef24e389002803eb23d903fb2da3) | kdrozd-dev |
| 2026-11-27 | [[xpu][UT] Route `zero_()` to a device memset (`zero_xpu_`) and enable…](https://github.com/pytorch/pytorch/commit/00a8c226f1e97ee56e1b8991d0c4944d3a9dd1f6) | hoshibara |
| 2026-11-27 | [[XPU] Run the remaining move_to_device_pass tests on all accelerators…](https://github.com/pytorch/pytorch/commit/d8b2a40f8d656f4fb58d74e2881aa03bab35a2ff) | tszulist-hbn |
| 2026-11-27 | [[cleanup] remove `__ubsan_ignore_float_divide_by_zero__` definition (…](https://github.com/pytorch/pytorch/commit/583804e13ff4d2ae0ba7d37f66929498c4a8743b) | khushi-411 |
| 2026-11-27 | [Retain the native group for the TokenSwitch handle lifetime (#204971)](https://github.com/pytorch/pytorch/commit/2cd56519bc79d6875925ba4d9d25b8cf331a0abe) | crcrpar |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
