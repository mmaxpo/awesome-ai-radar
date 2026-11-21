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
| 🐞 **Open issues + PRs** | [18.5k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1681.8 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 23d ago</sub>

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
| 2026-11-21 | [[CUDAGraph] Annotate captured memcpy batch nodes (#205997)](https://github.com/pytorch/pytorch/commit/00251bb0b7db29e3189176cfbbda482913270e79) | ngimel |
| 2026-11-21 | [[inductor] Cap the number of dynamic-shape sub-kernels per combo kern…](https://github.com/pytorch/pytorch/commit/cb41f4ef2382a6c77b67706485bf54ae613b8d76) | anijain2305 |
| 2026-11-21 | [[dynamo] Support bytearray is*() predicate methods (#205779)](https://github.com/pytorch/pytorch/commit/58a489fc6df58ef17de494dacf7ac452e7e34154) | Oscar-man-shrestha |
| 2026-11-21 | [[dynamo] Support bytearray.removeprefix() and bytearray.removesuffix(…](https://github.com/pytorch/pytorch/commit/3d9968a444014684a6e46fa9214f77255bcd42c6) | Oscar-man-shrestha |
| 2026-11-21 | [[MPS] Add float8_e8m0fnu and float4_e2m1fn_x2 as passthrough types (#…](https://github.com/pytorch/pytorch/commit/44574849bc88fb5332406f51d782c491f01259fc) | malfet |
| 2026-11-21 | [Reject shell dtype casts in TensorIterator on every device (#205864)](https://github.com/pytorch/pytorch/commit/0058429b37991a2946bd1b47b8f9fd0ea1458c26) | malfet |
| 2026-11-21 | [[torchtitan hash update] update the pinned torchtitan hash (#205963)](https://github.com/pytorch/pytorch/commit/b9945d7c319a6a68a9e4f44794490d6a4c74fb81) | pytorchupdatebot |
| 2026-11-21 | [[Inductor] Support ND pointwise and reduction tiling (#204324) (#204324)](https://github.com/pytorch/pytorch/commit/e716fffc7eded0e8ee852fbc2fa8a80ced15cf57) | blaine-rister |
| 2026-11-21 | [[inductor] Move AutotuneCache.save's entry serialization next to the …](https://github.com/pytorch/pytorch/commit/f893f94ec926bfc18409821af29d7bdad2ea9102) | bobrenjc93 |
| 2026-11-21 | [[aot autograd cache] Factor precompile artifact recording out of AOTA…](https://github.com/pytorch/pytorch/commit/e7a4eeee76cdbd5d32611ec074a620b211821cd4) | bobrenjc93 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
