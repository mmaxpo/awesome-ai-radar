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
| ⭐ **Stars** | 105.5k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.3k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1677.6 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 18d ago</sub>

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
| 2026-11-16 | [[dynamo] Preserve dictionary storage order and builtin representation…](https://github.com/pytorch/pytorch/commit/46ba0e8cab72c02cedacadaad780a8e3ad83e7bd) | XuehaiPan |
| 2026-11-16 | [[OpenReg] Rename OpenReg operator implementation files for clarity (#…](https://github.com/pytorch/pytorch/commit/561ce6ea6526ff9bf150e0acd8f8a8dab0cc640a) | can-gaa-hou |
| 2026-11-16 | [Revert "[CUDA][LinAlg] lu_factor: performance improvements for batche…](https://github.com/pytorch/pytorch/commit/a0d3a9fc144dc6ef10e95dfd6568ceef467af56c) | pytorchmergebot |
| 2026-11-16 | [[AOTI] Support PrivateUse1 devices in the model.so runtime (#204396)](https://github.com/pytorch/pytorch/commit/b82a2ed8e5d8672d1e4b1a39fec9320f20f0e01a) | can-gaa-hou |
| 2026-11-16 | [[CUDA][LinAlg] lu_factor: performance improvements for batched rectan…](https://github.com/pytorch/pytorch/commit/3b8c011f34e5bf837ad86d73ded03e9708aab07f) | nikitaved |
| 2026-11-16 | [[Test][XPU] Enable more `test_dataloader.py` tests on XPU (#203236)](https://github.com/pytorch/pytorch/commit/9c96ccf57a913f584b2042d9114caa4ffaa91c3b) | pbielak |
| 2026-11-16 | [[Test][XPU] Enable more `test_foreach.py` cases on XPU (#202763)](https://github.com/pytorch/pytorch/commit/68f0e54fd5ad3d7ceba57b36a5c2ebbacd3d6756) | pbielak |
| 2026-11-16 | [[Test][XPU] Enable more `nn/test_convolution.py` tests on XPU (#202750)](https://github.com/pytorch/pytorch/commit/06f9e25791bf2d23433b898dc153e13ed87bc38e) | pbielak |
| 2026-11-16 | [[7/N] Refactor `TestAOTModuleSimplifiedDevice` and enable on XPU (#19…](https://github.com/pytorch/pytorch/commit/eb0f3a479c877468051f6228e8b4c8819fbdde4a) | pbielak |
| 2026-11-16 | [Drop the unused torch::sycl CMake target (#195312)](https://github.com/pytorch/pytorch/commit/2395b41e0295e424ecd2484f4aa28ac2fcfcc21b) | cyyever |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
