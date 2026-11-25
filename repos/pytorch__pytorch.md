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
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.6k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1692.3 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 27d ago</sub>

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
| 2026-11-25 | [[ROCm]: Add Group Gemm Backend Selection Heuristic (#204242)](https://github.com/pytorch/pytorch/commit/be6edbd6b5c55cff0d852aa5e79d4dab4f450e5c) | TheRealMichaelWang |
| 2026-11-25 | [Document single-element tuple support in avg_pool3d docs (#206165)](https://github.com/pytorch/pytorch/commit/8e13fcc45bbca5421c7ab3f49068a5cad7d8110e) | rashedrana |
| 2026-11-25 | [Cross-reference the logistic sigmoid APIs in the PyTorch docs (#206287)](https://github.com/pytorch/pytorch/commit/bc8841896ea1493fb5b74caa786f9abc6b3e02b0) | chamione |
| 2026-11-25 | [[mkldnn][17/N] Port ideep's primitive cache and attr_t into ATen (#20…](https://github.com/pytorch/pytorch/commit/efd2c8f556dcd09b75104888aec9d5ca2cae9b10) | frost-intel |
| 2026-11-25 | [[mkldnn][16/N] Port ideep matmul (fp32 and quantized) into ATen (#205…](https://github.com/pytorch/pytorch/commit/872d189fe989d7b2479a861c3fc56937ab7922a9) | frost-intel |
| 2026-11-25 | [[mkldnn][15/N] Port ideep quantized transposed convolution into ATen …](https://github.com/pytorch/pytorch/commit/cfebc8d7e3e369fdd55f85dda536c8c1372b83a9) | frost-intel |
| 2026-11-25 | [[mkldnn][14/N] Port ideep transposed convolution into ATen (#205974)](https://github.com/pytorch/pytorch/commit/166b1f35ff221d2dbdd6dc500a25a2158e285181) | frost-intel |
| 2026-11-25 | [[mkldnn][13/N] Port ideep quantized convolution into ATen (#205973)](https://github.com/pytorch/pytorch/commit/ea5587c4e634d0ff9f5ea54e328f82b2745e9d81) | frost-intel |
| 2026-11-25 | [[mkldnn][12/N] Port ideep convolution compute_v2 into ATen (#205972)](https://github.com/pytorch/pytorch/commit/436f47e152bad7e279352262c04e9561f7dbdc66) | frost-intel |
| 2026-11-25 | [added lowering for adaptive_avg_pool2d_backward (#201075)](https://github.com/pytorch/pytorch/commit/2acfb36e361a8140e7d57224da94266664e681be) | morrison-turnansky |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
