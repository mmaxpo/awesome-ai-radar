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
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1681.4 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 20d ago</sub>

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
| 2026-11-18 | [[Testcase Refactoring] Classify test/test_ops_gradients.py for the te…](https://github.com/pytorch/pytorch/commit/6dd0379803abe6a1735af5158733806413c1598b) | KarhouTam |
| 2026-11-18 | [[Testcase Refactoring] Classify test/profiler/test_torch_tidy.py for …](https://github.com/pytorch/pytorch/commit/9a9f91b071da771cd7fd7ca62fc2a0e8295877d9) | KarhouTam |
| 2026-11-18 | [[export] Document that export does not record an outer autocast (#205…](https://github.com/pytorch/pytorch/commit/42d36d305cc6a9e16aa1812c0bab5cc7a5acd59f) | shoumikhin |
| 2026-11-18 | [[xpu] Remove unused function in grouped_mm (#205485)](https://github.com/pytorch/pytorch/commit/57f02f8db4f8ab613f55826dd1235500147f6681) | LuFinch |
| 2026-11-18 | [[inductor] Add module_fqns and weight_fqns to kernel_information.json…](https://github.com/pytorch/pytorch/commit/93fdc6758e5513edcd0d86a09e313b5aca05bd64) | MirrorZ |
| 2026-11-18 | [[inductor] Return Integer(0) from TruncToInt(Float(0.0)) (#204784)](https://github.com/pytorch/pytorch/commit/19c8216e9b1ed4face6ed9ae45f30aa08d38f6a8) | saitejacodes |
| 2026-11-18 | [[Testcase Refactoring] Make test_split_cat_fx_passes device-agnostic …](https://github.com/pytorch/pytorch/commit/f2e0555046e9ffd90aaf091f3148422b18849760) | gavinwang269 |
| 2026-11-18 | [[CPP FakeTensor] Skip unsupported nested tensor tests (#205364)](https://github.com/pytorch/pytorch/commit/d0f3e6fa71f2f56e5ab8b64052ddd9f91bbd9f88) | liangel-02 |
| 2026-11-18 | [[export] Preserve sparse functorch wrappers in fake snapshots (#204957)](https://github.com/pytorch/pytorch/commit/2ec8123e7d87eaecd27ab9f4f8f0cbdb6cdea481) | liangel-02 |
| 2026-11-18 | [[CPP FakeTensor] Support nested operator argument and output containe…](https://github.com/pytorch/pytorch/commit/8096046d4b8b968c09f4bdac4c73d95af0098e34) | liangel-02 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
